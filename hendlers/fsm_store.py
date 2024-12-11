from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from buttons import cansel_markup
from aiogram.types import ReplyKeyboardRemove


class FSMstore(StatesGroup):
    model_name = State()
    size = State()
    category = State()
    price = State()
    photo = State()
    submit = State()


async def start_fsm_store(message: types.Message):
    await message.answer('Какую модель вы хотите?', reply_markup=cansel_markup)
    await FSMstore.model_name.set()


async def load_model_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['model_name'] = message.text

    await FSMstore.next()
    await message.answer('Какой размер вы хотите?')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await FSMstore.next()
    await message.answer('Какую категорию вы хотите выбрать?')


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await FSMstore.next()
    await message.answer('Какую цену вы хотите выбрать?')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await FSMstore.next()
    await message.answer('Отправьте фото устройства, которое вы хотите приобрести.')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await FSMstore.next()
    await message.answer('Проверьте, все ли данные верны? (Введите "Да" или "Нет")')


async def load_submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        async with state.proxy() as data:
            await message.answer(f"Ваши данные сохранены: {data}")
        await state.finish()
    elif message.text.lower() == 'нет':
        await message.answer('Регистрация отменена.')
        await state.finish()
    else:
        await message.answer('Введите "Да" или "Нет"!')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=ReplyKeyboardRemove())


def register_fsmreg_handlers(dp: Dispatcher):
    dp.register_message_handler(start_fsm_store, commands=['regist'], state=None)
    dp.register_message_handler(load_model_name, state=FSMstore.model_name)
    dp.register_message_handler(load_size, state=FSMstore.size)
    dp.register_message_handler(load_category, state=FSMstore.category)
    dp.register_message_handler(load_price, state=FSMstore.price)
    dp.register_message_handler(load_photo, state=FSMstore.photo, content_types=['photo'])
    dp.register_message_handler(load_submit, state=FSMstore.submit)
    dp.register_message_handler(cancel_fsm, Text(equals='отмена', ignore_case=True), state='*')
