# Подключаем класс pipeline из модуля transformers библиотеки Hugging Face.
from transformers import pipeline

# Создаем пайплайн, используя конструктор pipeline.
question_answerer = pipeline('question-answering')

# Загружаем текст, в котором будет ответ на задаваемый вопрос.
context = """
Vladimir Putin, in full Vladimir Vladimirovich Putin, (born October 7, 1952, Leningrad, Russia, U.S.S.R. [now St. Petersburg, Russia]), Russian intelligence officer and politician who served as president (1999–2008, 2012– ) of Russia and also was the country’s prime minister (1999, 2008–12).

Early career
Putin studied law at Leningrad State University, where his tutor was Anatoly Sobchak, later one of the leading reform politicians of the perestroika period. Putin served 15 years as a foreign intelligence officer for the KGB (Committee for State Security), including six years in Dresden, East Germany. In 1990 he retired from active KGB service with the rank of lieutenant colonel and returned to Russia to become prorector of Leningrad State University with responsibility for the institution’s external relations. Soon afterward Putin became an adviser to Sobchak, the first democratically elected mayor of St. Petersburg. He quickly won Sobchak’s confidence and became known for his ability to get things done; by 1994 he had risen to the post of first deputy mayor.

In 1996 Putin moved to Moscow, where he joined the presidential staff as deputy to Pavel Borodin, the Kremlin’s chief administrator. Putin grew close to fellow Leningrader Anatoly Chubais and moved up in administrative positions. In July 1998 Pres. Boris Yeltsin made Putin director of the Federal Security Service (FSB; the KGB’s domestic successor), and shortly thereafter he became secretary of the influential Security Council. Yeltsin, who was searching for an heir to assume his mantle, appointed Putin prime minister in 1999.

Although he was virtually unknown, Putin’s public-approval ratings soared when he launched a well-organized military operation against secessionist rebels in Chechnya. Wearied by years of Yeltsin’s erratic behaviour, the Russian public appreciated Putin’s coolness and decisiveness under pressure. Putin’s support for a new electoral bloc, Unity, ensured its success in the December parliamentary elections.

"""

# Вопрос.
question = "When was Vladimir Putin born?"

# Используем пайплайн в переменной question_answerer для ответа на вопрос.
print(question_answerer(question=question, context=context))