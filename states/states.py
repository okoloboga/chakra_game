from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

# Создаем класса, наследуемый от StatesGroup для группы состояний в FSM
class FSMMain(StatesGroup):

    state_1 = State()              
    state_2 = State()            