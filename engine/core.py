from typing import Callable, Dict, List

from engine.types import AbstractAction, AbstractSession, Performance
from engine.glide import StoryMap

from adt import adt, Case


class HistorySession(AbstractSession):
    history: List[str]
    progress: Dict[str, int]


class NarrativeMachine:
    def __init__(self, session: HistorySession,
                 glide_map: StoryMap,
                 prefix_callback: Callable[[AbstractSession, AbstractAction], None],
                 error_callback: Callable[[BaseException, str, int, AbstractSession, AbstractAction], AbstractAction],
                 end_callback: Callable[[AbstractSession], None],
                 play_all=False):

        self.session = session
        self.glide_map = glide_map

        self.prefix_callback = prefix_callback
        self.error_callback = error_callback
        self.end_callback = end_callback

        if not self.session.history:
            self.session.history.append('entry')
            self.session.progress['entry'] = 0

        self.play_all = play_all
        self.bound = False

        self.session.last_action = None

    def next_action(self) -> AbstractAction:

        """
        almost immutable method of getting next action
        """

        if not self.session.history:
            return None

        self.state = self.session.history[-1]
        self.progress = self.session.progress[self.state]

        current_glide = self.glide_map[self.state]

        if self.progress >= len(current_glide):
            # just pops history states which is no more valid
            self.session.history.pop()
            return self.next_action()
        else:
            return current_glide[self.progress]

    # move one step forward -- either in the current glide or jumping to another
    def _step(self, new_state=None):
        self.session.progress[self.state] += 1

        if new_state:
            self.session.history.append(new_state)
            if new_state not in self.session.progress:
                self.session.progress[new_state] = 0

    # bind callback
    def _bind(self, bind_cb: Callable[[Callable], None], after_cb: Callable):
        self.bound = True
        self._after_resume = after_cb
        self._step()
        return bind_cb(self.session, lambda: self.run(resume=True))

    def run(self, resume=False):

        # if resuming
        if self.bound and resume:
            self._after_resume(self.session)
            self.bound = False

        # action loop
        while not self.bound:

            # get action
            action = self.next_action()

            # if no more actions
            if action is None:
                return self.end_callback(self.session)

            # if action is not playing - skip
            if not self.play_all and not action.is_actual(self.session):
                self._step()
                continue

            # before performing action
            self.prefix_callback(self.session, action)

            # try to perform action
            try:
                result = action.perform(self.session)
            except BaseException as e:
                # except some shit
                self.error_callback(e, self.state, self.progress, self.session, action)
                self._step()
            else:
                # last successful action
                self.session.last_action = action

                # process action result
                result.match(
                    move_on=self._step,
                    bind=self._bind,
                    jump=self._step,
                    jump_sub=lambda name: self._step(new_state=f"<{name}"),
                )
