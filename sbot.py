import asyncio
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, \
    CallbackQuery, Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

a = Bot(token="8958110452:AAFz1pbTyQFg3a4Nem4h6Sd7LoMPQRoWpuM")
dp = Dispatcher()

btn1 = KeyboardButton(text="Вибір інструменту")
btn2 = KeyboardButton(text="Список пісень")
btn3 = KeyboardButton(text="Пошук акордів")

users = {}
kb = ReplyKeyboardMarkup(keyboard=[[btn1, btn2], [btn3]])

guitarChords = {
    'C':'''1 струна - 0
    2 струна - 1
    3 струна - 0
    4 струна - 2
    5 струна - 3
    6 струна - X''',

    'Cm':'''1 струна - 3
    2 струна - 4
    3 струна - 5
    4 струна - 5
    5 струна - 3
    6 струна - X''',

    'D':'''1 струна - 2
    2 струна - 3
    3 струна - 2
    4 струна - 0
    5 струна - X
    6 струна - X''',

    'Dm':'''1 струна - 1
    2 струна - 3
    3 струна - 2
    4 струна - 0
    5 струна - X
    6 струна - X''',

    'E':'''1 струна - 0
    2 струна - 0
    3 струна - 1
    4 струна - 2
    5 струна - 2
    6 струна - 0''',

    'Em':'''1 струна - 0
    2 струна - 0
    3 струна - 0
    4 струна - 2
    5 струна - 2
    6 струна - 0''',

    'F':'''1 струна - 1
    2 струна - 1
    3 струна - 2
    4 струна - 3
    5 струна - 3
    6 струна - 1''',

    'Fm':'''1 струна - 1
    2 струна - 1
    3 струна - 1
    4 струна - 3
    5 струна - 3
    6 струна - 1''',

    'G':'''1 струна - 3
    2 струна - 0
    3 струна - 0
    4 струна - 0
    5 струна - 2
    6 струна - 3''',

    'Gm':'''1 струна - 3
    2 струна - 3
    3 струна - 3
    4 струна - 5
    5 струна - 5
    6 струна - 3''',

    'A':'''1 струна - 0
    2 струна - 2
    3 струна - 2
    4 струна - 2
    5 струна - 0
    6 струна - X''',

    'Am':'''1 струна - 0
    2 струна - 1
    3 струна - 2
    4 струна - 2
    5 струна - 0
    6 струна - X''',

    'B':'''1 струна - 1
    2 струна - 3
    3 струна - 3
    4 струна - 3
    5 струна - 1
    6 струна - X''',

    'Bm':'''1 струна - 2
    2 струна - 3
    3 струна - 4
    4 струна - 4
    5 струна - 2
    6 струна - X'''
}

ukuleleChords = {
    'A':'''G - 2
    C - 1
    E - 0
    A - 0''',

    'Am':'''G - 2
    C - 0
    E - 0
    A - 0''',

    'B':'''G - 4
    C - 3
    E - 2
    A - 2''',

    'Bm':'''G - 4
    C - 2
    E - 2
    A - 2''',

    'C':'''G - 0
    C - 0
    E - 0
    A - 3''',

    'Cm':'''G - 0
    C - 3
    E - 3
    A - 3''',

    'D':'''G - 2
    C - 2
    E - 2
    A - 0''',

    'Dm':'''G - 2
    C - 2
    E - 1
    A - 0''',

    'E':'''G - 1
    C - 4
    E - 0
    A - 2''',

    'Em':'''G - 0
    C - 4
    E - 3
    A - 2''',

    'F':'''G - 2
    C - 0
    E - 1
    A - 0''',

    'Fm':'''G - 1
    C - 0
    E - 1
    A - 3''',

    'G':'''G - 0
    C - 2
    E - 3
    A - 2''',

    'Gm':'''G - 0
    C - 2
    E - 3
    A - 1'''
}




btn = [
    [
        InlineKeyboardButton(text="Гітара", callback_data="button_1_pressed")
    ],
    [
        InlineKeyboardButton(text="Укулеле", callback_data="button_2_pressed")
    ]
]
kb2 = InlineKeyboardMarkup(inline_keyboard=btn)

btn3 = [
    [
        InlineKeyboardButton(text="'Perfect' - Ed Sheeran", callback_data="button_3_pressed")
    ],
    [
        InlineKeyboardButton(text="'Let her go' - Passenger", callback_data="button_4_pressed")
    ],
    [
        InlineKeyboardButton(text="'Let it be' - The Beatles", callback_data="button_5_pressed")
    ]
]
kb3 = InlineKeyboardMarkup(inline_keyboard=btn3)


@dp.message(F.text == "/start")
async def start(message: Message, state: FSMContext):
    await message.answer(
        "Привіт! Ласкаво просимо до «Збірника акордів»! Тут ти можеш швидко знайти акорди до улюблених пісень, переглянути тексти, підібрати тональність та вдосконалювати свою гру на гітарі. Просто напиши назву пісні або виконавця, і я допоможу знайти потрібні акорди.")
    await message.answer("Виберіть дію", reply_markup=kb)


@dp.message(F.text == "Вибір інструменту")
async def inst(message: Message):
    await message.answer("Виберіть інструмент", reply_markup=kb2)


@dp.callback_query(F.data == "button_1_pressed")
async def prs1(callback_query: CallbackQuery):
    await callback_query.message.answer("Ви вибрали гітару")
    users[callback_query.from_user.id] = 1


@dp.callback_query(F.data == "button_2_pressed")
async def prs2(callback_query: CallbackQuery):
    await callback_query.message.answer("Ви вибрали укулеле")
    users[callback_query.from_user.id] = 0

@dp.message(F.text == "Пошук акордів")
async def chord(message: Message):
    await message.answer("Напишіть акорд")

@dp.message()
async def search(message: Message):

    user_id = message.from_user.id
    chords = message.text

    if user_id not in users:
        await message.answer("Спочатку виберіть інструмент")
        return

    if users[user_id] == 1:
        await message.answer(guitarChords[chords])

    elif users[user_id] == 0:
        await message.answer(ukuleleChords[chords])

@dp.message(F.text == "Список пісень")
async def song(message: Message):
    await message.answer("Виберіть пісню", reply_markup=kb3)


@dp.callback_query(F.data == "button_3_pressed")
async def prs3(callback_query: CallbackQuery):
    await callback_query.message.answer('''[Intro]
G

[Verse 1]
          G        Em
I found a love for me
              C                            D
Darling, just dive right in, and follow my lead
                G          Em
Well, I found a girl beautiful and sweet
        C                                     D
I never knew you were the someone waiting for me

[Pre-Chorus]
                                G
Cause we were just kids when we fell in love
            Em                      C                G  D
Not knowing what it was, I will not give you up this ti-ime
             G                           Em
Darling just kiss me slow, your heart is all I own
            C                     D
And in your eyes you're holding mine

[Chorus]
      Em   C             G          D              Em
Baby, I'm dancing in the dark, with you between my arms
C                G     D                Em
Barefoot on the grass, listening to our favourite song
          C                G                 D              Em
When you said you looked a mess, I whispered underneath my breath
         C                G        D          G
But you heard it, darling you look perfect tonight

|(G) D/F# Em D | C  D  |

[Verse 2]
                G                    Em
Well, I found a woman, stronger than anyone I know
              C                                          D
She shares my dreams, I hope that someday I'll share her home
           G             Em
I found a love, to carry more than just my secrets
         C                              D
To carry love, to carry children of our own

[Pre-Chorus]
                             G                     Em
We are still kids, but we're so in love, fighting against all odds
             C               G  D
I know we'll be alright this ti-ime
             G                              Em
Darling just hold my hand, be my girl, I'll be your man
         C               D
I see my future in your eyes

[Chorus]
      Em   C              G         D              Em
Baby, I'm dancing in the dark, with you between my arms
C                G     D                Em
Barefoot on the grass, listening to our favourite song
        C                G                D
When I saw you in that dress, looking so beautiful
  Em       C                  G        D          G
I don't deserve this, darling you look perfect tonight

[Interlude]
|(G) | G | Em | % |
| C  | % | D  | % |

[Chorus]
      Em   C              G         D              Em
Baby, I'm dancing in the dark, with you between my arms
C                G     D                Em
Barefoot on the grass, listening to our favourite song
        C              G               D             Em
I have faith in what I see, now I know I have met an angel
    C          G         D
In person, and she looks perfect

[Outro]
  G/B     C           Dsus4    D          G
I don't deserve this, you look perfect tonight

|(G) D/F# Em D | C  D  | G''')


@dp.callback_query(F.data == "button_4_pressed")
async def prs4(callback_query: CallbackQuery):
    await callback_query.message.answer('''                   F                       C
Well you only need the light when it s burning low
              G                       Am
Only miss the sun when it s starts to snow
               F                           C       G
Only know your love her when you let her Go
                      F                        C
Only know you ve been high when you re feeling low
              G                        Am
Only hate the road when you re missin  home
               F                         C
Only know your love her when you ve let her Go
G
  And you let her Go

Am   F   G   Em
Am   F   G

Am                            F
Staring at the bottom of your glass
        G                            Em
Hoping one day you will make a dream last
               Am               F          G
The dreams come slow and goes so fast
    Am                          F
You see her when you close your eyes
      G                           Em
Maybe one day you will understand why
               Am           F         G
Everything you touch surly dies

                       F                       C
Well you only need the light when it s burning low
              G                       Am
Only miss the sun when it s starts to snow
               F                           C       G
Only know your love her when you let her Go
                      F                        C
Only know you ve been high when you re feeling low
              G                        Am
Only hate the road when you re missin  home
               F                         C
Only know your love her when you ve let her Go
Am                            F
Staring at the ceiling in the dark
         G                     Em
Same old empty feeling in your heart
           Am                 F       G
Love comes slow and it goes so fast
         Am                      F
Well you see her when you fall asleep
                G                  Em
But to never to touch and never to keep
                         Am
Because you loved her to much
                 F          G
And you dive too deep

                       F                       C
Well you only need the light when it s burning low
              G                       Am
Only miss the sun when it s starts to snow
               F                           C       G
Only know your love her when you let her Go
                      F                        C
Only know you ve been high when you re feeling low
              G                        Am
Only hate the road when you re missin  home
               F                         C
Only know your love her when you ve let her Go

                Am
And you let her Go
      F     G
Ooooo ooooo oooooo
                Am
And you let her Go
        F     G
Ooooooo ooooo ooooo
                Am         F    G   Em
And you let her Go


Am    F    G

                       F                       C
Well you only need the light when it s burning low
              G                       Am
Only miss the sun when it s starts to snow
               F                           C       G
Only know your love her when you let her Go
                      F                        C
Only know you ve been high when you re feeling low
              G                        Am
Only hate the road when you re missin  home
               F                         C
Only know your love her when you ve let her Go
G
  And you let her Go

                       F                       C
Well you only need the light when it s burning low
              G                       Am
Only miss the sun when it s starts to snow
               F                           C       G
Only know your love her when you let her Go
                      F                        C
Only know you ve been high when you re feeling low
              G                        Am
Only hate the road when you re missin  home
               F                         C
Only know your love her when you ve let her Go
G                             Am
  And you let her go''')


@dp.callback_query(F.data == "button_5_pressed")
async def prs5(callback_query: CallbackQuery):
    await callback_query.message.answer('''[Verse 1]
C                     G                 Am     Am7  F
When I find myself in times of trouble, Mother Mary comes to me
C                 G              F  (Hit E note on D string)(Hit D String) C
Speaking words of wisdom, let it be
C                 G                Am       Am7      F
And in my hour of darkness, She is standing right in front of me
C                 G              F  (Hit E note on D string)(Hit D String) C
Speaking words of wisdom, Let it be

[Chorus]
       Am         G          F          C
Let it be, let it be, let it be, let it be
C                G              F (Hit E note on D string)(Hit D String) C
Whisper words of wisdom, let it be

[Verse 2]
C                   G               Am        Am7       F
And when the broken hearted people, Living in the world agree
C                G              F  (Hit E note on D string)(Hit D String) C
There will be an answer, let it be
C                   G               Am        Am7       F
But though they may be parted, There is still a chance that they will see
C                G              F  (Hit E note on D string)(Hit D String) C
There will be an answer, let it be

[Chorus]
       Am         G          F          C
Let it be, let it be, let it be, let it be
C                G              F (Hit E note on D string)(Hit D String) C
There will be an answer, let it be
Am         G          F          C
Let it be, let it be, let it be, let it be
C                G              F (Hit E note on D string)(Hit D String) C
Whisper words of wisdom, let it be
[Chorus]
       Am         G          F          C
Let it be, let it be, let it be, let it be
C                G              F (Hit E note on D string)(Hit D String) C
Whisper words of wisdom, let it be

[Verse 3]
C                   G                  Am            Am7  F
And when the night is cloudy, there is still a light that shines on me
C                G              F  (Hit E note on D string)(Hit D String) C
Shine on till tomorrow, let it be
C                   G                   Am   Am7      F
I wake up to the sound of music, Mother Mary comes to me
C                G              F  (Hit E note on D string)(Hit D String) C
Speaking words of wisdom, let it be

[Chorus]
       Am         G          F          C
Let it be, let it be, let it be, let it be
C                G              F (Hit E note on D string)(Hit D String) C
Whisper words of wisdom, let it be
Am         G          F          C
Let it be, let it be, let it be, let it be
C                G              F (Hit E note on D string)(Hit D String) C
Whisper words of wisdom, let it be

That's right, BOTH SOLOS! And they're right.
Listen to the songs for timing. Rock on...''')







async def main():
    await dp.start_polling(a)


asyncio.run(main())