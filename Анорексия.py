# coding=utf-8
import telebot
from telebot import types
import time

bot = telebot.TeleBot(token.txt)


@bot.message_handler(commands=['start'])
def otpravlu(message):
    bot.send_message(message.chat.id, f'Привет,если у тебя возникла проблема с расстройством пищевого поведения,тебе ко мне. Я хочу подчеркнуть, что правильное питание играет важную роль в вашем выздоровлении, и я готов помочь вам в этом процессе. \n\n❤️Помните, что каждый из вас уникален, и я предлагаю персонализированный подход к вашему питанию, чтобы помочь вам восстановить здоровые отношения с едой❤️.')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Что такое анорексия?")
    btn2 = types.KeyboardButton("Что такое РПП?")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Давай сначала узнаем что такое Анорексия и РПП, и с их причинами.', reply_markup=markup)
    
@bot.message_handler(commands=['terms'])
def jklist_commands(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Что такое анорексия?")
    btn2 = types.KeyboardButton("Что такое РПП?")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, '👇👇', reply_markup=markup)
 
@bot.message_handler(commands=['question'])
def darya(message):   
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text="❤️", url= 'https://t.me/pourewddcvjgdsdgbjjjj')
    markup.add(button1)
    bot.send_message(message.chat.id, f'Не сравнивайте себя с другими и не стремитесь к идеалу. Важно любить себя таким, какой вы есть, и заботиться о своем здоровье. Помните, что вес - это всего лишь один из множества показателей, определяющих ваше здоровье. Важнее следить за своим общим физическим и эмоциональным состоянием. Занимайтесь любимыми видами спорта, правильно питайтесь и не забывайте о самопринятии. Вы прекрасны такие, какие есть, и никакой вес не может изменить это. Будьте здоровы и счастливы!', reply_markup=markup)

@bot.message_handler(commands=['food'])
def pitanie(message):
    file = open('1d0d7910-63f9-4eee-a12c-d86f2e09d224.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    # markup = telebot.types.InlineKeyboardMarkup()
    # button1 = telebot.types.InlineKeyboardButton(text="❤️", url= 'https://t.me/pourewddcvjgdsdgbjjjj')
    # markup.add(button1)
    bot.send_message(message.chat.id, "Правильное питание играет ключевую роль в поддержании здоровья и благополучия. Вот несколько основных принципов правильного питания:\n\n1. Разнообразие\n\n2. Овощи и фрукты\n\n3. Зерновые продукты\n\n4. Белки\n\n5. Здоровые жиры\n\n6. Ограничение сахара и процессированных продуктов\n\n7. Умеренность\n\n8. Питьевой режим\n\nЭти принципы помогут поддерживать здоровый образ жизни и обеспечивать организм всем необходимым для правильного функционирования.")
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text="❤️", url= 'https://t.me/pourewddcvjgdsdgbjjjj')
    markup.add(button1)
    bot.send_message(message.chat.id, "Если ты хотешь узнать больше о здоровом питании, то подписывайся на канал ❤️")

@bot.message_handler(commands=['ves'])
def pitanie(message):
    file = open('1ffab718-b3f1-43dc-9423-f6ad109b5ee3.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    bot.send_message(message.chat.id, "Нормальный вес - это вес, который соответствует здоровому состоянию организма и позволяет человеку выполнять свои ежедневные функции без напряжения и усталости. Он зависит от множества факторов, включая возраст, пол, физическую активность, наличие заболеваний и генетические предрасположенности.")

@bot.message_handler(commands=['treatment'])
def metod(message):
    file = open('98b889a3-a6b1-4a34-ad7c-288eb0c5fccc.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    bot.send_message(message.chat.id, "<b>Методы лечения анорексии</b>\n\n1. Психотерапия\n\n2. Семейная терапия\n\n3. Фармакотерапия\n\n4. Питание и диетотерапия\n\n5. Медицинский наблюдательный контроль\n\n6. Поддержка группы\n\nВажно помнить, что каждый человек уникален, и нет единого подхода к лечению анорексии, который подходит всем. Врачи и специалисты по психическому здоровью должны индивидуально оценивать каждого пациента и разрабатывать наиболее подходящий план лечения.", parse_mode='html')

@bot.message_handler(commands=['muslu'])
def muslu(message):
    file = open('29d1c602-09ea-4c02-bc61-a5a4f2814f09.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    bot.send_message(message.chat.id, "<b>Тревоги и негативные мысли о еде</b>\n\n1. Попробуйте сделать список своих мыслей о еде и отметить Каждый шаг вте, которые вызывают у вас тревогу или негативные эмоции. \n\n2. Постарайтесь заменить негативные мысли на более позитивные.\n\n3. Избегайте сравнений с другими людьми или стандартами красоты.\n\n4. Практикуйте медитацию или другие методы релаксации, чтобы снять напряжение и тревогу.\n\n5. Не думайте о еде как о враге или вещи, которую нужно контролировать. \n\n6. Обратитесь за помощью к специалисту, если ваши мысли о еде вызывают сильную тревогу и мешают вам жить полноценной жизнью.\n\n7. Помните, что каждый день - новый шанс начать с чистого листа и принять здоровые решения для своего тела и разума. Не позволяйте негативным мыслям о еде влиять на вашу жизнь.\n\n8. Изучите основы правильного питания и попробуйте включить их в свой рацион.\n\n9. Не пропускайте приемы пищи и не ставьте себя на строгую диету.\n\n10. Не стесняйтесь просить помощи у близких и друзей, если вам трудно справляться с мыслями о еде. Иметь поддержку и понимание окружающих очень важно для преодоления любых трудностей.\n\n11. Сосредоточьтесь на своих достижениях и прогрессе, а не на неудачах или ошибках.\n\n12. Не забывайте об умеренности.\n\n13. Не думайте о своем теле как о чем-то, что нужно постоянно улучшать или менять.\n\n14. Не забывайте о физической активности. Регулярные занятия спортом помогут вам поддерживать здоровое тело и улучшать настроение.\n\n15. Не ставьте себе запреты на любимую еду. Разрешите себе наслаждаться ею в разумных количествах и без чувства вины.", parse_mode='html')

@bot.message_handler(commands=['approach'])
def approach(message):
    file = open('c1ef104c-286c-4c2b-84b7-60561ed4c89a.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    bot.send_message(message.chat.id, "<b>Психологические подходы к негативным мыслям о еде</b>\n\n1. Когнитивно-поведенческий подход.\n\n2. Подход мотивации к действию.\n\n3. Подход медитации и майндфулнесс.\n\n4. Подход саморегуляции.\n\n5. Подход психообразования. \n\nВажно помнить, что каждый человек уникален и может потребоваться комбинация различных подходов для преодоления негативных мыслей о еде. Лучше всего обратиться за помощью к профессиональному психологу или диетологу, который поможет разработать индивидуальную программу работы с негативными мыслями о еде.\n\n\nПодробнее о психологических подходов вы можете узнать в нашем канале", parse_mode='html')

@bot.message_handler(commands=['list'])
def list_commands(message):
    bot.send_message(message.chat.id, 'это список команд которые тебе доступны:\n\n/terms - понятия Анорексии и РПП, и их причины.\n\n/question - если есть какие то вопросы и нужна помощь.\n\n/info - информация о боте')


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Что такое анорексия?"):
        markup = telebot.types.InlineKeyboardMarkup()
        btn = telebot.types.InlineKeyboardButton(text="Причины", callback_data="button1")
        markup.add(btn)
        bot.send_message(message.chat.id, f"Анорексия - это расстройство пищевого поведения, характеризующееся намеренным отказом от пищи, стремлением к крайне низкому весу и искажением своего собственного телосознания. Люди, страдающие анорексией, обычно ощущают сильный страх набирать вес или принимать пищу.", reply_markup=markup)
    elif(message.text == "Что такое РПП?"):
        markup = telebot.types.InlineKeyboardMarkup()
        but = telebot.types.InlineKeyboardButton(text="Причины РПП", callback_data="button2")
        markup.add(but)
        bot.send_message(message.chat.id, text="Расстройства пищевого поведения (РПП) - это группа психических заболеваний, связанных с неправильным отношением к еде, включающих не только анорексию, но и булимию, компульсивное переедание и другие подобные", reply_markup=markup)






# @bot.callback_query_handler(func=lambda call: True)
# def handle_callback_query(message):
#     if(message.text == "Причины"):
#         bot.send_message(message.chat.id, "frhg")



# @bot.message_handler(commands=['calendar'])
# def get_calendar(message):
#     now = datetime.datetime.now() #Текущая дата
#     chat_id = message.chat.id
#     date = (now.year,now.month)
#     current_shown_dates[chat_id] = date #Сохраним текущую дату в словарь
#     markup = create_calendar(now.year,now.month)
#     bot.send_message(message.chat.id, "Пожалйста, выберите дату", reply_markup=markup)






# # Обычный режим
# @bot.message_handler(content_types=["text"])
# def any_msg(message):
#     keyboard = types.InlineKeyboardMarkup()
#     callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
#     keyboard.add(callback_button)
#     bot.send_message(message.chat.id, "Я – сообщение из обычного режима", reply_markup=keyboard)


# # Инлайн-режим с непустым запросом
# @bot.inline_handler(lambda query: len(query.query) > 0)
# def query_text(query):
#     kb = types.InlineKeyboardMarkup()
#     # Добавляем колбэк-кнопку с содержимым "test"
#     kb.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="test"))
#     results = []
#     single_msg = types.InlineQueryResultArticle(
#         id="1", title="Press me",
#         input_message_content=types.InputTextMessageContent(message_text="Я – сообщение из инлайн-режима"),
#         reply_markup=kb
#     )
#     results.append(single_msg)
#     bot.answer_inline_query(query.id, results)


# # В большинстве случаев целесообразно разбить этот хэндлер на несколько маленьких
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     # Если сообщение из чата с ботом
#     if call.message:
#         if call.data == "test":
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")
#     # Если сообщение из инлайн-режима
#     elif call.inline_message_id:
#         if call.data == "test":
#             bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")    
    
    
# @bot.message_handler(content_types=['text'])
# def start(message):
#      if message.text == 'Причины':
#         kb = types.InlineKeyboardMarkup(row_width=1)
#         btn = types.InlineKeyboardButton(text='KHonka 1', callback_data='btn1')
#         btn1 = types.InlineKeyboardButton(text='KHonka 2', callback_data='btn2')
#         kb.add(btn, btn1)
#         bot.send_message(message.chat.id, '1', reply_markup=kb)

# @bot.message_handler(commands=['start'])
# def start(message):
#     kb = types.InlineKeyboardMarkup(row_width=1)
#     btn = types.InineKeyboardButton(text='KHonka 1', callback_data='btn1')
#     btn1 = types.InlineKeyboardButton(text='KHonka 2', callback_data='btn2')
#     kb.add(btn, btn1)
#     bot.send_message(message.chat.id, '1', reply_markup=kb)

# @bot.callback_query_handler(func=lambda callback: callback.data)
# def check_callback_data(callback):
#     if callback.data == 'button1':
#         kb = types.InlineKeyboardMarkup(row_width=1)
#         btn = types.InlineKeyboardButton(text='Генетические', callback_data='batn1')
#         btn1 = types.InlineKeyboardButton(text='Биологические', callback_data='batn2')
#         btn2 = types.InlineKeyboardButton(text='Микросоциальные', callback_data='batn3')
#         btn3 = types.InlineKeyboardButton(text='Личностный', callback_data='batn4')
#         btn4 = types.InlineKeyboardButton(text='Культурные', callback_data='batn5')
#         btn5 = types.InlineKeyboardButton(text='Стрессовые', callback_data='batn6')
#         kb.add(btn, btn1, btn2, btn3 ,btn4, btn5)
#         bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='HoBui texte', reply_markup=kb)
#         if callback.data == 'batn1':
#             bot.send_message(callback.message.chat.id, '1')

# # Обработчик коллбэка
# @bot.callback_query_handler(func=lambda call: True)
# def callback_handler(call):
#     if call.data == 'button1':
#         bot.send_message(call.message.chat.id, "Причины бывают разные")
#         markup = types.InlineKeyboardMarkup()
#         item2 = types.InlineKeyboardButton("Новая кнопка", callback_data='button2')
#         markup.add(item2)
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= "Причины бывают ра", reply_markup=markup)
#         bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Причины')
#         kb = types.InlineKeyboardMarkup(row_width=1)
#         btn = types.InlineKeyboardButton(text='Генетические', callback_data='batn1')
#         btn1 = types.InlineKeyboardButton(text='Биологические', callback_data='batn2')
#         btn2 = types.InlineKeyboardButton(text='Микросоциальные', callback_data='batn3')
#         btn3 = types.InlineKeyboardButton(text='Личностный', callback_data='batn4')
#         btn4 = types.InlineKeyboardButton(text='Культурные', callback_data='batn5')
#         btn5 = types.InlineKeyboardButton(text='Стрессовые', callback_data='batn6')
#         kb.add(btn, btn1, btn2, btn3 ,btn4, btn5)
#         bot.send_message(call.message.chat.id, "Djn ghbxbys", reply_markup=kb)
# # Обработчик коллбэка для новой кнопки
# @bot.callback_query_handler(func=lambda call: call.data)
# def callback_handler_new_button(call):
#     if call.data == 'button2':
#         bot.send_message(call.message.chat.id, "Ты нажал новую кнопку!")


# @bot.message_handler(content_types=['text'])
# def inline_key(message):






@bot.message_handler(content_types=['text'])
def func1(message):
    if(message.text == "Что такое анорексия?"):
        markup = telebot.types.InlineKeyboardMarkup()
        btn = telebot.types.InlineKeyboardButton(text="Причины", callback_data="button1")
        markup.add(btn)
        bot.send_message(message.chat.id, f"Анорексия - это расстройство пищевого поведения, характеризующееся намеренным отказом от пищи, стремлением к крайне низкому весу и искажением своего собственного телосознания. Люди, страдающие анорексией, обычно ощущают сильный страх набирать вес или принимать пищу.", reply_markup=markup)
    elif(message.text == "Что такое РПП?"):
        markup = telebot.types.InlineKeyboardMarkup()
        but = telebot.types.InlineKeyboardButton(text="Причины РПП", callback_data="button2")
        markup.add(but)
        bot.send_message(message.chat.id, text="Расстройства пищевого поведения (РПП) - это группа психических заболеваний, связанных с неправильным отношением к еде, включающих не только анорексию, но и булимию, компульсивное переедание и другие подобные", reply_markup=markup)
    elif(message.text == "Вопросы"):
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="❤️", url= 'https://t.me/owiwwksjjdhdbsbd')
        markup.add(button1)
        bot.send_message(message.chat.id, f'Пиши ей', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "button1":
        bot.send_message(call.message.chat.id, 'Причины бывают разные и их много',  reply_markup=types.ReplyKeyboardRemove())
        mainmenu = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Генетические', callback_data='key1')
        key2 = types.InlineKeyboardButton(text='Биологические', callback_data='key2')
        mainmenu.add(key1, key2)
        key3 = types.InlineKeyboardButton(text='Микросоциальные', callback_data='key3')
        key4 = types.InlineKeyboardButton(text='Личностный', callback_data='key4')
        mainmenu.add(key3, key4)
        key5 = types.InlineKeyboardButton(text='Культурные', callback_data='key5')
        key6 = types.InlineKeyboardButton(text='Стрессовые', callback_data='key6')
        mainmenu.add(key5, key6)
        bot.send_message(call.message.chat.id, 'Давай познакомимся с ними 👇', reply_markup=mainmenu)
     
    elif call.data == "mainmenu":
        mainmenu = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Генетические', callback_data='key1')
        key2 = types.InlineKeyboardButton(text='Биологические', callback_data='key2')
        mainmenu.add(key1, key2)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=mainmenu)
        
    elif call.data == "key1": #При нажатии Генетические                                 
        next_menu = types.InlineKeyboardMarkup()
        key3 = types.InlineKeyboardButton(text='Биологические', callback_data='key2')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menu.add(key3,  back)
        bot.edit_message_text('<b>Генетические.</b>\n\nВероятность болезни определяется несколькими генами, регулирующими нейрохимические факторы пищевых расстройств поведения. К настоящему моменту изучен ген НТR2A, кодирующий серотониновый рецептор, и ген BDNF, влияющий на активность гипоталамуса. Существует генетическая детерминированность определенных черт характера, предрасполагающих к заболеванию.!', call.message.chat.id, call.message.message_id, parse_mode='html', 
                            reply_markup=next_menu)
    elif call.data == "key2": #При нажатии Биологические
        next_menu2 = types.InlineKeyboardMarkup()
        key4 = types.InlineKeyboardButton(text='Микросоциальные', callback_data='key3')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menu2.add(key4, back)
        bot.edit_message_text('<b>Биологические.</b>\n\nПищевое поведение чаще нарушено у людей с избыточной массой тела, ожирением и ранним наступлением менархе. В основе лежит дисфункция нейромедиаторов (серотонина, дофамина, норадреналина) и чрезмерная выработка лептина – гормона, снижающего аппетит.', call.message.chat.id, call.message.message_id, parse_mode='html',
                            reply_markup=next_menu2)
    elif call.data == "key3": #При нажатии Микросоциальные
        next_menu3 = types.InlineKeyboardMarkup()
        key5 = types.InlineKeyboardButton(text='Личностные', callback_data='key4')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menu3.add(key5, back)
        bot.edit_message_text('<b>Микросоциальные.</b>\n\nВажную роль в развитии заболевания играет отношение родителей и других родственников к питанию, лишнему весу и худобе. Анорексия чаще встречается в семьях, где у родственников имеется подтвержденный диагноз заболевания, где демонстрируется пренебрежение едой, отказы принимать пищу.', call.message.chat.id, call.message.message_id, parse_mode='html' ,
                            reply_markup=next_menu3)
    elif call.data == "key4": #При нажатии Личностные
        next_menu4 = types.InlineKeyboardMarkup()
        key6 = types.InlineKeyboardButton(text='Культурные', callback_data='key5')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menu4.add(key6, back)
        bot.edit_message_text('<b>Личностные.</b>\n\nРасстройству более подвержены лица с обсессивно-компульсивным типом личности. Стремление к худобе, голодание, изнуряющие нагрузки поддерживаются перфекционизмом, низкой самооценкой, неуверенностью, тревожностью и мнительностью.', call.message.chat.id, call.message.message_id, parse_mode='html' ,
                            reply_markup=next_menu4)
    elif call.data == "key5": #При нажатии Культурные
        next_menu5 = types.InlineKeyboardMarkup()
        key6 = types.InlineKeyboardButton(text='Стрессовые', callback_data='key6')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menu5.add(key6, back)
        bot.edit_message_text('<b>Культурные.</b>\n\nВ индустриально развитых странах худоба провозглашается одним из главных критериев красоты женщины. Идеалы стройного тела пропагандируются на разных уровнях, формируя у молодежи стремление похудеть любым способом.', call.message.chat.id, call.message.message_id, parse_mode='html' ,
                            reply_markup=next_menu5)
    elif call.data == "key6": #При нажатии Стрессовые
        next_menu6 = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenumda')
        next_menu6.add(back)
        bot.edit_message_text('<b>Стрессовые</b>\n\nПусковым фактором анорексии может стать смерть близкого человека, сексуальное или физическое насилие. В подростковом и молодом возрасте причиной является неуверенность в будущем, невозможность достижения желаемых целей. Процесс похудения замещает сферы жизни, в которых пациенту не удается реализовать себя.', call.message.chat.id, call.message.message_id, parse_mode='html' ,
                            reply_markup=next_menu6)
        bot.send_message(call.message.chat.id, "После того как ты познакомился с анорексией, давай познакомимся с РПП.")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Что такое анорексия?")
        btn2 = types.KeyboardButton("Что такое РПП?")
        markup.add(btn1, btn2)
        bot.send_message(call.message.chat.id, 'Нажимай на клавиатуру снизу.' ,reply_markup=markup)

    elif call.data == "button2":
        bot.send_message(call.message.chat.id, 'РПП может быть вызвана различными факторами, включая генетические, психологические и окружающие условия. ',  reply_markup=types.ReplyKeyboardRemove())
        mainmenu2 = types.InlineKeyboardMarkup()
        key7 = types.InlineKeyboardButton(text='Генетика', callback_data='key7')
        key8 = types.InlineKeyboardButton(text='Психологические факторы', callback_data='key8')
        mainmenu2.add(key7, key8)
        key9 = types.InlineKeyboardButton(text='Социокультурные факторы', callback_data='key9')
        key10 = types.InlineKeyboardButton(text='Травмы и стресс', callback_data='key10')
        mainmenu2.add(key9, key10)
        key11 = types.InlineKeyboardButton(text='Другие психические расстройства', callback_data='key11')
        key12 = types.InlineKeyboardButton(text='Проблемы с обменом веществ', callback_data='key12')
        mainmenu2.add(key11, key12)
        key13 = types.InlineKeyboardButton(text='Культурные различия', callback_data='key13')
        mainmenu2.add(key13)
        bot.send_message(call.message.chat.id, 'Вот некоторые из наиболее распространенных причин РПП:',
                            reply_markup=mainmenu2)
    elif call.data == "mainmenu11":
        mainmenu11 = types.InlineKeyboardMarkup()
        key7 = types.InlineKeyboardButton(text='Генетика', callback_data='key7')
        key8 = types.InlineKeyboardButton(text='Психологические факторы', callback_data='key8')
        mainmenu11.add(key7, key8)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=mainmenu11)
    elif call.data == "key7": #При нажатии Генетика                             
        next_menu = types.InlineKeyboardMarkup()
        key8 = types.InlineKeyboardButton(text='Психологические фактор', callback_data='key8')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu11')
        next_menu.add(key8,  back)
        bot.edit_message_text('<b>Генетика.</b>\n\nИсследования показывают, что у людей с РПП часто есть близкие родственники с этим расстройством, что указывает на возможное наследственное влияние.', call.message.chat.id, call.message.message_id, parse_mode='html', 
                            reply_markup=next_menu)
    elif call.data == "key8": #При нажатии Психологические фактор                            
        next_menu0 = types.InlineKeyboardMarkup()
        key9 = types.InlineKeyboardButton(text='Социокультурные факторы', callback_data='key9')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu11')
        next_menu0.add(key9,  back)
        bot.edit_message_text('<b>Психологические факторы.</b>\n\nНизкая самооценка, стремление к совершенству и проблемы с контролем импульсов могут способствовать развитию РПП.', call.message.chat.id, call.message.message_id, parse_mode='html', 
                            reply_markup=next_menu0)
    elif call.data == "key9": #При нажатии Социокультурные факторы
        next_menu2 = types.InlineKeyboardMarkup()
        key4 = types.InlineKeyboardButton(text='Травмы и стресс', callback_data='key10')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu11')
        next_menu2.add(key4, back)
        bot.edit_message_text('<b>Социокультурные факторы.</b>\n\nДавление общества на идеальную фигуру и красоту может влиять на развитие РПП, особенно у женщин.', call.message.chat.id, call.message.message_id, parse_mode='html',
                            reply_markup=next_menu2)
    elif call.data == "key10": #При нажатии Травмы и стресс
        next_menu3 = types.InlineKeyboardMarkup()
        key5 = types.InlineKeyboardButton(text='Другие психические расстройства', callback_data='key11')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu11')
        next_menu3.add(key5, back)
        bot.edit_message_text('<b>Травмы и стресс.</b>\n\nТравматические события или высокий уровень стресса могут быть причиной РПП у некоторых людей.', call.message.chat.id, call.message.message_id, parse_mode='html' ,
                            reply_markup=next_menu3)
    elif call.data == "key11": #При нажатии Другие психические расстройства
        next_menu4 = types.InlineKeyboardMarkup()
        key6 = types.InlineKeyboardButton(text='Проблемы с обменом веществ', callback_data='key12')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu11')
        next_menu4.add(key6, back)
        bot.edit_message_text('<b>Другие психические расстройства.</b>\n\nРПП часто сопровождается другими психическими расстройствами, такими как депрессия, тревожность и нарушения личности.', call.message.chat.id, call.message.message_id, parse_mode='html' ,
                            reply_markup=next_menu4)
    elif call.data == "key12": #При нажатии Проблемы с обменом веществ
        next_menu5 = types.InlineKeyboardMarkup()
        key6 = types.InlineKeyboardButton(text='Культурные различия', callback_data='key13')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu11')
        next_menu5.add(key6, back)
        bot.edit_message_text('<b>Проблемы с обменом веществ.</b>\n\nНекоторые исследования показывают, что у людей с РПП может быть нарушен обмен веществ, что может влиять на их отношение к еде и весу.', call.message.chat.id, call.message.message_id, parse_mode='html' ,
                            reply_markup=next_menu5)
    elif call.data == "key13": #При нажатии Культурные различия
        next_menu7 = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu11')
        next_menu7.add(back)
        bot.edit_message_text('<b>Культурные различия.</b>\n\nРПП наблюдается в разных культурах, но может проявляться по-разному в зависимости от социокультурных факторов.', call.message.chat.id, call.message.message_id, parse_mode='html' ,
                             reply_markup=next_menu7)
        bot.send_message(call.message.chat.id, "Важно отметить, что РПП обычно вызывается комбинацией различных факторов, а не одной конкретной причиной. Поэтому для успешного лечения необходимо учитывать все эти факторы и работать с пациентом над их решениемВажно отметить, что РПП обычно вызывается комбинацией различных факторов, а не одной конкретной причиной. Поэтому для успешного лечения необходимо учитывать все эти факторы и работать с пациентом над их решением")
    






# РПП может быть вызвана различными факторами, включая генетические, психологические и окружающие условия. Вот некоторые из наиболее распространенных причин РПП:

# 1. Генетика: исследования показывают, что у людей с РПП часто есть близкие родственники с этим расстройством, что указывает на возможное наследственное влияние.

# 2. Психологические факторы: низкая самооценка, стремление к совершенству и проблемы с контролем импульсов могут способствовать развитию РПП.

# 3. Социокультурные факторы: давление общества на идеальную фигуру и красоту может влиять на развитие РПП, особенно у женщин.4

# 4. Травмы и стресс: травматические события или высокий уровень стресса могут быть причиной РПП у некоторых людей.97

# 5. Другие психические расстройства: РПП часто сопровождается другими психическими расстройствами, такими как депрессия, тревожность и нарушения личности.uo[]

# 6. Проблемы с обменом веществ: некоторые исследования показывают, что у людей с РПП может быть нарушен обмен веществ, что может влиять на их отношение к еде и весу.

# 7. Культурные различия: РПП наблюдается в разных культурах, но может проявляться по-разному в зависимости от социокультурных факторов.

# Важно отметить, что РПП обычно вызывается комбинацией различных факторов, а не одной конкретной причиной. Поэтому для успешного лечения необходимо учитывать все эти факторы и работать с пациентом над их решением



# @bot.message_handler(commands=['list'])
# def list_commands(message):
#     bot.send_message(message.chat.id, 'это список команд которые тебе доступны:\n\n/question - если есь какие то вопросы и нужна помощь')

# @bot.message_handler(commands=['five'])
# def gdnsl(message):
#     bot.send_message(message.chat.id, "поздравляю с днем рождения брат, чтоб всегда все было хорошо, чтоб все было как ты хочешь, чтоб была удача и благополучие, больше оптимизма, позитива и вдохновения. чтоб была любовь и радость, чтоб не сломила любая гадость. Пусть все твои желания сбываются, пусть все будет так, как ты захочешь.\n\nЖмякай /six")


# @bot.message_handler(content_types=['text'])
# def inline_key(a):
#     if a.text == "Inline_menu":
#         mainmenu = types.InlineKeyboardMarkup()
#         key1 = types.InlineKeyboardButton(text='Кнопка 1', callback_data='key1')
#         key2 = types.InlineKeyboardButton(text='Кнопка 2', callback_data='key2')
#         mainmenu.add(key1, key2)
#         bot.send_message(a.chat.id, 'Это главное меню!', reply_markup=mainmenu)

# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     if call.data == "mainmenu":
#         mainmenu = types.InlineKeyboardMarkup()
#         key1 = types.InlineKeyboardButton(text='Кнопка 1', callback_data='key1')
#         key2 = types.InlineKeyboardButton(text='Кнопка 2', callback_data='key2')
#         mainmenu.add(key1, key2)
#         bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=mainmenu)
#     elif call.data == "key1":
#         next_menu = types.InlineKeyboardMarkup()
#         key3 = types.InlineKeyboardButton(text='Кнопка 3', callback_data='key3')
#         back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
#         next_menu.add(key3, back)
#         bot.edit_message_text('Это меню уровня 2, для кнопки1!', call.message.chat.id, call.message.message_id,
#                               reply_markup=next_menu)
#     elif call.data == "key2":
#         next_menu2 = types.InlineKeyboardMarkup()
#         key4 = types.InlineKeyboardButton(text='Кнопка 4', callback_data='key4')
#         back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
#         next_menu2.add(key4, back)
#         bot.edit_message_text('Это меню уровня 2, для кнопки2!', call.message.chat.id, call.message.message_id,
#                               reply_markup=next_menu2)



# @bot.callback_query_handler(func=lambda callback: True)
# def check_callback_data(callback):
#     if callback.data == "button1":
#         kb = types.InlineKeyboardMarkup(row_width=1)
#         btn = types.InlineKeyboardButton(text='Генетические', callback_data='batn1')
#         btn1 = types.InlineKeyboardButton(text='Биологические', callback_data='batn2')
#         btn2 = types.InlineKeyboardButton(text='Микросоциальные', callback_data='batn3')
#         btn3 = types.InlineKeyboardButton(text='Личностный', callback_data='batn4')
#         btn4 = types.InlineKeyboardButton(text='Культурные', callback_data='batn5')
#         btn5 = types.InlineKeyboardButton(text='Стрессовые', callback_data='batn6')
#         kb.add(btn, btn1, btn2, btn3 ,btn4, btn5)
#         markup1 = telebot.types.InlineKeyboardMarkup()
#         knp = types.InlineKeyboardButton(text='exit', callback_data='back_menu')
#         markup1.add(knp)
#         bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Вероятность болезни определяется несколькими генами, регулирующими нейрохимические факторы пищевых расстройств поведения. К настоящему моменту изучен ген НТR2A, кодирующий серотониновый рецептор, и ген BDNF, влияющий на активность гипоталамуса. Существует генетическая детерминированность определенных черт характера, предрасполагающих к заболеванию.\n/exit', reply_markup=markup1)
#         if callback.data == 'batn2':
#             markup2 = telebot.types.InlineKeyboardMarkup()
#             knp = types.InlineKeyboardButton(text='exit', callback_data='back_menu')
#             markup2.add(knp)
#             bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Пищевое поведение чаще нарушено у людей с избыточной массой тела, ожирением и ранним наступлением менархе. В основе лежит дисфункция нейромедиаторов (серотонина, дофамина, норадреналина) и чрезмерная выработка лептина – гормона, снижающего аппетит.\n/exit', reply_markup=markup2)
#         elif callback.data == 'batn3':
#             markup3 = telebot.types.InlineKeyboardMarkup()
#             knp = types.InlineKeyboardButton(text='exit', callback_data='back_menu')
#             markup3.add(knp)
#             bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Важную роль в развитии заболевания играет отношение родителей и других родственников к питанию, лишнему весу и худобе. Анорексия чаще встречается в семьях, где у родственников имеется подтвержденный диагноз заболевания, где демонстрируется пренебрежение едой, отказы принимать пищу.\n/exit', reply_markup=markup3)
#         elif callback.data == 'batn4':
#             markup4 = telebot.types.InlineKeyboardMarkup()
#             knp = types.InlineKeyboardButton(text='exit', callback_data='back_menu')
#             markup4.add(knp)
#             bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Расстройству более подвержены лица с обсессивно-компульсивным типом личности. Стремление к худобе, голодание, изнуряющие нагрузки поддерживаются перфекционизмом, низкой самооценкой, неуверенностью, тревожностью и мнительностью.\n/exit', reply_markup=markup4)
#         elif callback.data == 'batn5':
#             markup5 = telebot.types.InlineKeyboardMarkup()
#             knp = types.InlineKeyboardButton(text='exit', callback_data='back_menu')
#             markup5.add(knp)
#             bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='В индустриально развитых странах худоба провозглашается одним из главных критериев красоты женщины. Идеалы стройного тела пропагандируются на разных уровнях, формируя у молодежи стремление похудеть любым способом.\n/exit', reply_markup=markup5)
#         elif callback.data == 'batn5':
#             markup6 = telebot.types.InlineKeyboardMarkup()
#             knp = types.InlineKeyboardButton(text='exit', callback_data='back_menu')
#             markup6.add(knp)
#             bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Пусковым фактором анорексии может стать смерть близкого человека, сексуальное или физическое насилие. В подростковом и молодом возрасте причиной является неуверенность в будущем, невозможность достижения желаемых целей. Процесс похудения замещает сферы жизни, в которых пациенту не удается реализовать себя.\n/exit', reply_markup=markup6)


# @bot.callback_query_handler(func=lambda callback: True)
# def check_callback_dat(callback):
#     if callback.data == "back_menu":
#         markup = telebot.types.InlineKeyboardMarkup()
#         btn = telebot.types.InlineKeyboardButton(text="Генетические", callback_data="button1")
#         btn1 = types.InlineKeyboardButton(text='Биологические', callback_data='batn2')
#         btn2 = types.InlineKeyboardButton(text='Микросоциальные', callback_data='batn3')
#         btn3 = types.InlineKeyboardButton(text='Личностный', callback_data='batn4')
#         btn4 = types.InlineKeyboardButton(text='Культурные', callback_data='batn5')
#         btn5 = types.InlineKeyboardButton(text='Стрессовые', callback_data='batn6')
#         markup.add(btn, btn1, btn2, btn3, btn4, btn5)
#         bot.send_message(callback.message.chat.id, f"Анорексия - это расстройство пищевого поведения, характеризующееся намеренным отказом от пищи, стремлением к крайне низкому весу и искажением своего собственного телосознания. Люди, страдающие анорексией, обычно ощущают сильный страх набирать вес или принимать пищу.\n\nТакже у анорексии бывают разные причины", reply_markup=markup)


# @bot.message_handler(commands=['exit'])
# def check_call(message):
#         markup = telebot.types.InlineKeyboardMarkup()
#         btn = telebot.types.InlineKeyboardButton(text="Генетические", callback_data="button1")
#         btn1 = types.InlineKeyboardButton(text='Биологические', callback_data='batn2')
#         btn2 = types.InlineKeyboardButton(text='Микросоциальные', callback_data='batn3')
#         btn3 = types.InlineKeyboardButton(text='Личностный', callback_data='batn4')
#         btn4 = types.InlineKeyboardButton(text='Культурные', callback_data='batn5')
#         btn5 = types.InlineKeyboardButton(text='Стрессовые', callback_data='batn6')
#         markup.add(btn, btn1, btn2, btn3, btn4, btn5)
#         bot.send_message(message.chat.id, f"Анорексия - это расстройство пищевого поведения, характеризующееся намеренным отказом от пищи, стремлением к крайне низкому весу и искажением своего собственного телосознания. Люди, страдающие анорексией, обычно ощущают сильный страх набирать вес или принимать пищу.\n\nТакже у анорексии бывают разные причины", reply_markup=markup)

# @bot.callback_query_handler(func=lambda callback: callback.data == 'back_menu')
# def check_callback_dat(callback):
#     markup = types.InlineKeyboardMarkup()
#     btn = types.InlineKeyboardButton(text="Генетические", callback_data="button1")
#     btn1 = types.InlineKeyboardButton(text='Биологические', callback_data='batn2')
#     btn2 = types.InlineKeyboardButton(text='Микросоциальные', callback_data='batn3')
#     btn3 = types.InlineKeyboardButton(text='Личностный', callback_data='batn4')
#     btn4 = types.InlineKeyboardButton(text='Культурные', callback_data='batn5')
#     btn5 = types.InlineKeyboardButton(text='Стрессовые', callback_data='batn6')
#     markup.add(btn, btn1, btn2, btn3, btn4, btn5)
#     bot.send_message(callback.message.chat.id, "Анорексия - это расстройство пищевого поведения, характеризующееся намеренным отказом от пищи, стремлением к крайне низкому весу и искажением своего собственного телосознания. Люди, страдающие анорексией, обычно ощущают сильный страх набирать вес или принимать пищу.\n\nТакже у анорексии бывают разные причины", reply_markup=markup)






# @bot.callback_query_handler(func=lambda callback: callback.data)
# def check_callback_dat(callback):

# @bot.message_handler(content_types=['text'])
# def start(message):
#      if message.text == 'Генетические':
#         kb = types.InlineKeyboardMarkup(row_width=1)
#         btn = types.InlineKeyboardButton(text='KHonka 1', callback_data='btn1')
#         btn1 = types.InlineKeyboardButton(text='KHonka 2', callback_data='btn2')
#         kb.add(btn, btn1)
#         bot.send_message(message.chat.id, '1', reply_markup=kb)

    
# @bot.callback_query_handler(func=lambda callback: callback.data)
# def check_callback_dat(callback):
#     if callback.data == "batn1":
#         bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Причины бывают разные и их очень много')
#     elif callback.data =='batn2':
#         bot.send_message(message.chat.id, text='кнопка 2')
#     elif callback.data =='batn2':
#         bot.send_message(message.chat.id, text='кнопка 3')
#     elif callback.data =='batn2':
#         bot.send_message(message.chat.id, text='кнопка 4')
#     elif callback.data =='batn2':
#         bot.send_message(message.chat.id, text='кнопка 5')
#     elif callback.data =='batn2':
#         bot.send_message(message.chat.id, text='кнопка 6')



bot.polling(non_stop=True)

# Генетические. Вероятность болезни определяется несколькими генами, регулирующими нейрохимические факторы пищевых расстройств поведения. К настоящему моменту изучен ген НТR2A, кодирующий серотониновый рецептор, и ген BDNF, влияющий на активность гипоталамуса. Существует генетическая детерминированность определенных черт характера, предрасполагающих к заболеванию.
#   Биологические. Пищевое поведение чаще нарушено у людей с избыточной массой тела, ожирением и ранним наступлением менархе. В основе лежит дисфункция нейромедиаторов (серотонина, дофамина, норадреналина) и чрезмерная выработка лептина – гормона, снижающего аппетит.
#   Микросоциальные. Важную роль в развитии заболевания играет отношение родителей и других родственников к питанию, лишнему весу и худобе. Анорексия чаще встречается в семьях, где у родственников имеется подтвержденный диагноз заболевания, где демонстрируется пренебрежение едой, отказы принимать пищу.
#   Личностный. Расстройству более подвержены лица с обсессивно-компульсивным типом личности. Стремление к худобе, голодание, изнуряющие нагрузки поддерживаются перфекционизмом, низкой самооценкой, неуверенностью, тревожностью и мнительностью.
#   Культурные. В индустриально развитых странах худоба провозглашается одним из главных критериев красоты женщины. Идеалы стройного тела пропагандируются на разных уровнях, формируя у молодежи стремление похудеть любым способом.
#   Стрессовые. Пусковым фактором анорексии может стать смерть близкого человека, сексуальное или физическое насилие. В подростковом и молодом возрасте причиной является неуверенность в будущем, невозможность достижения желаемых целей. Процесс похудения замещает сферы жизни, в которых пациенту не удается реализовать себя.}














