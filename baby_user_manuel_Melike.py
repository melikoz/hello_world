import random
import time

"""
This program aims to provide a suggestion cheat-sheet for most common baby problems
for the concerned mama -or papa :)
It aims to identify the reason for the problem and make a suggestion accordingly.

The program starts by receiving 'age and name of the baby' as input from the user.
Then it will list the most common problems according to the age of the baby
and ask the user to choose the one that best defines the problem.
Then this input is used to come up with a suggestion.
A problem can be repeated at different ages of the baby but the underlying reason and accordingly the suggestion
might be different. So the reasons and suggestions to be provided as the output are generated according to the age.


The program also aims to strike a relaxing, sympathetic tone by means of providing statements reflecting empathy
and fun. 

"""


CHOICE_COUNT = 3

def main():
    greet()
    name_and_age = basic_info()
    iteration(name_and_age)
    farewell()

def greet():
    greetings1 = []
    gree1_A = "Hello mama!"
    gree1_B = "Hi there!"
    greetings1.append(gree1_A)
    greetings1.append(gree1_B)

    greetings2 = []
    gree2_A = "Got a bit of a headache, do we? \n"
    gree2_B = "Concerned about the lil'one, you are? \n"
    greetings2.append(gree2_A)
    greetings2.append(gree2_B)

    greetings3 = []
    gree3_A = "Let's see if I can help you.. \n"
    gree3_B = "I'd be so glad if I can help you.. \n"
    greetings3.append(gree3_A)
    greetings3.append(gree3_B)

    part_1 = greetings1[random.randint(0, (len(greetings1)-1))]
    part_2 = greetings2[random.randint(0, (len(greetings2) - 1))]
    part_3 = greetings3[random.randint(0, (len(greetings3) - 1))]
    print("\n=================================================")
    print("=  ===========  BABY USER MANUAL =============  =")
    print("=================================================")
    print("\n"+ part_1 + " " + part_2)
    time.sleep(1)
    print(part_3)
    time.sleep(2)


def basic_info():
    # this step is to learn the age and name  of the baby
    nicknames = ["pumpkin", "munchkin", "angel"]
    adoration = ["Sweet!", "Lovely name!", "How cute!"]
    baby_nick = nicknames[random.randint(0, (len(nicknames)-1))]
    baby_adore = adoration[random.randint(0, (len(adoration)-1))]
    baby_name = str(input("So what is the name of the little " + baby_nick + "? \n"))
    baby_age = int(input("\n"+ baby_adore + " And how old is " + baby_name + " in weeks? \n"))

    # we create a dictionary with the name and age of the baby and pass it to the next function
    name_and_age = {baby_name: baby_age}
    return name_and_age

def iteration(name_and_age):
    # this will have 4 steps to be completed:
    # 1) find out the symptoms by making the user choose from the program's suggestions
    # 2) match the possible reason(s) for the chosen symptom(s), that is reach some sort of a diagnosis
    # 3) suggest an action
    # 4) ask if there are more concerns. if yes, ask whether for the same baby, if yes, repeat the iteration function
    #   if another baby, repeat from basic_info function

    name_list = list(name_and_age.keys())
    age = name_and_age.get(name_list[0])
    name = name_list[0]

    if age <= 12:
        print("\nWhich of the following best describes "+ name+ "'s problem?")
        time.sleep(1)

        choices = ["A", "B", "C"]
        # most common problems for 0-12 weeks babies:
        a = "Baby cries for no reason"
        b = "Baby breathes too fast"
        c = "Baby falls asleep while nursing"
        d = "It hurts while baby is nursing"
        e = "Baby cries in sleep"
        f = "Baby doesn't pee or poo enough"
        problems_0_12_weeks = [a, b, c, d, e, f]


        # diagnosis related to the most common problems for 0-12 weeks babies
        normal = "It's normal.. babies do that.."
        warning = "Sounds a bit concerning.."
        x = "New borns hardly have any other problem other than hunger or wet diaper."
        y = normal
        z = normal
        t = "That's probably because the baby doesn't latch properly"
        u = normal
        v = warning
        diagnosis_0_12_weeks = [x, y, z, t, u, v]

        # suggestions for the diagnosed problems for 0-12 weeks babies
        k = "Check the baby's fever and carefully observe their body to see if there's anything that bothers them physically. \n" \
            "If these are not the reasons then it's most probably really just hunger. And if feeding also doesn't help then they're, well, being a baby! \n" \
            "Just chill, give them a warm hug and enjoy that gorgeous new born smell! :) "
        l = "But why are you awake when the baby is asleep? Stop watching the baby sleeping and close your eyes already! :) "
        m = "Keeping them awake is tricky and sometimes brutal but absolutely necessary. Try tickling their feet \n " \
            "or gently blowing to their hair. If it's warm enough, you can gently sprinkle drops of water to their arms or legs. \n" \
            "They probably won't appreciate being woken up but don't feel bad, it's for their own good! And you're doing right!"
        n = "It's normal to feel uncomfortable while breastfeeding at first. But if you continue feeling pain then it's not right. \n" \
            "It's crucial that the baby latches properly, not only for you to avoid pain but also for the baby to feed sufficiently. \n" \
            "Do not live with the pain! If you have access to a lactation consultant, book a randez-vous right away. \n " \
            "If you don't, work on your holding the baby.. Here is a good video that can guide you from YouTube: \n" \
            "https://youtu.be/u7Ufl1XR1Qg"
        o = "But why are you awake when the baby is asleep? Stop watching the baby sleeping and close your eyes already! :) "
        p = "Most probably baby isn't hydrated or fed enough. Have you changed something in the course of feeding? \n" \
            "If so, you might want to revert that.. Been skipping feeding sessions for the sake of sleep maybe? \n " \
            "If so, do not do that.. If the baby continue to produce less than 8 wet diapers a day, call your doctor right away. "
        suggestions_0_12_weeks = [k, l, m, n, o, p]

        for xx in range (CHOICE_COUNT):
                print("\n"+ choices[xx] + " "+ problems_0_12_weeks[xx])
                time.sleep(1)
        print("\nD None of these"+ "\n")
        concern = input("A, B, C or D? \n")

        if concern == "D" or concern == "d":
            print("\nHow about these?")
            for xx in range(CHOICE_COUNT):
                print("\n"+ choices[xx] + " " + problems_0_12_weeks[xx+ CHOICE_COUNT])
                time.sleep(1)
            print("\nD None of these" + "\n")
            concern2 = input("A, B, C or D? \n")
            if concern2 == "D" or concern2 == "d":
                print("\nI'm sorry but I'm afraid I can't help you with this one.. \n")
            if concern2 == "A" or concern2 == "B" or concern2 == "C":
                concern_mapping = {"A": 0+CHOICE_COUNT, "B": 1+CHOICE_COUNT, "C": 2+CHOICE_COUNT}
                position = concern_mapping.get(concern2)
                print("\n"+ diagnosis_0_12_weeks[position] + suggestions_0_12_weeks[position])
        if concern == "A" or concern == "B" or concern == "C":
            concern_mapping = {"A": 0, "B": 1, "C": 2}
            position = concern_mapping.get(concern)
            print("\n"+ diagnosis_0_12_weeks[position] + suggestions_0_12_weeks[position])
        more_questions(name_and_age)


    if age >= 13:
        print("\nWhich of the following best describes " + name + "'s problem?")
        time.sleep(1)

        choices = ["A", "B", "C"]

        # most common problems for 13-24 weeks babies:
        aa = "Baby cries inconsolably for no apparent reason"
        bb = "Baby wants to eat A LOT! Like really A LOT..."
        cc = "Baby doesn’t respond to visual stimulation"
        dd = "Baby can’t sit up on their own"
        ee = "Baby doesn’t want to breastfeed"
        ff = "Baby has dandruff like things on his head"
        problems_13_24_weeks = [aa, bb, cc, dd, ee, ff]

        # diagnosis related to the most common problems for 13-24 weeks babies
        normal = "It's normal.. babies do that.."
        warning = "Sounds a bit concerning.."
        xxx = "Don’t panic but your baby might be colicky.."
        yy = normal
        zz = warning
        tt = "You’re not skipping the tummy time, are you?"
        uu = "Oops! Bottle might be leading the competition.."
        vv = "It’s probably cradle cap, don’t worry.."
        diagnosis_13_24_weeks = [xxx, yy, zz, tt, uu, vv]

        # suggestions for the diagnosed problems for 13-24 weeks babies:
        kk = "Sure it’s annoying but it’s not the end of the world. Your baby is healthy and this will pass. \n" \
             "There’s not really any treatment but you might want to make it easier for everyone by holding the baby up, \n" \
             "walking around while holding them, keep the room’s lights dim, avoid stimulating sounds. And being patient.. :) "
        ll = "Babies might want to eat even more frequently and/or more if they are going through something called cluster feeding \n" \
             "It looks strange but it’s totally ok. Just chill and let the baby feed as much as they want."
        mm = "The visual capabilities of the baby are still not completely developed -and won’t be for quiet some time \n" \
             "but if they don’t respond to visual stimulations within 8 to 15 inches you might want to contact your pediatrician."
        nn = "Babies are not supposed to start sitting up independently before 6 months so don’t worry. \n " \
             "But the tummy time exercises are crucial for your baby’s physical development and you should \n" \
             "continue doing them around 30 minutes everyday, although you can divide them into parts."
        oo = "Baby is growing at a crazy speed during these weeks and their need for feeding increases as well. \n" \
             "It’s possible that mama’s body is lagging behind in providing extra milk. It’s ok, don’t be harsh on yourself, \n " \
             "this race is not lost yet. You have to satisfy baby’s hunger so bottle may take a bigger role during this time.\n" \
             "But continue to offer breast every time as your body needs the proximity of the baby to continue producing milk. \n" \
             "Moreover, your body will know that more is needed when your baby sucks for prolonged time and \n" \
             "express dissatisfaction in the end -yes, by means of crying out loud.. Also, continue pumping religiously. \n" \
             "You can also try tea’s and cookies but nothing works as good as pumping."
        pp = "Cradle cap is totally harmless and will go away on its own soon. For now, shampooing the scalp of the baby \n" \
             "and brushing would also help"
        suggestions_13_24_weeks = [kk, ll, mm, nn, oo, pp]

        for xx in range (CHOICE_COUNT):
                print("\n"+ choices[xx] + " "+ problems_13_24_weeks[xx])
                time.sleep(1)
        print("\nD None of these"+ "\n")
        concern = input("A, B, C or D? \n")

        if concern == "D" or concern == "d":
            print("\nHow about these?")
            for xx in range(CHOICE_COUNT):
                print("\n"+ choices[xx] + " " + problems_13_24_weeks[xx+ CHOICE_COUNT])
                time.sleep(1)
            print("\nD None of these" + "\n")
            concern2 = input("A, B, C or D? \n")
            if concern2 == "D" or concern2 == "d":
                print("\nI'm sorry but I'm afraid I can't help you with this one..")
            if concern2 == "A" or concern2 == "B" or concern2 == "C":
                concern_mapping = {"A": 0+CHOICE_COUNT, "B": 1+CHOICE_COUNT, "C": 2+CHOICE_COUNT}
                position = concern_mapping.get(concern2)
                print("\n"+ diagnosis_13_24_weeks[position] + suggestions_13_24_weeks[position])
        if concern == "A" or concern == "B" or concern == "C":
            concern_mapping = {"A": 0, "B": 1, "C": 2}
            position = concern_mapping.get(concern)
            print("\n"+ diagnosis_13_24_weeks[position] + suggestions_13_24_weeks[position])
        more_questions(name_and_age)

def more_questions(name_and_age):
    answer = input("\nDo you have more concerns that I can help you with? Yes or no please.. :) \n")
    if answer == "yes":
        name_list = list(name_and_age.keys())
        age = name_and_age.get(name_list[0])
        name = name_list[0]
        answer2 = input("\nSure! Is it about "+ name + "? Yes or no please.. \n")
        if answer2 == "yes":
            iteration(name_and_age)
        else:
            newbaby = basic_info()
            iteration(newbaby)

def farewell():
    # provide a farewell statement to the user when they choose there are no more concerns
    print("\n================================================================")
    print("Well, hope I've been of some help. Good luck with your treasure!")
    print("================================================================")

if __name__ == '__main__':
    main()