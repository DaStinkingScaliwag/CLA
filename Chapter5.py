from itertools import permutations as perm
class CLA:
    @staticmethod
    def questionOne(sticks):
        correct = 0
        total = 0
        for a, b, c in set([*perm(sticks, 3)]):
            if a+b>c and b+c>a and c+a>b:
                correct += 1
            total += 1
        return (correct/total)*100

    @staticmethod
    def questionTwo():
        sticks = [1, 3, 5, 7, 9]
        answer = []
        numberCorrect = 0
        for n in range(1, 16):
            for i in range(5):
                test = [stick for stick in sticks]
                test[i] = n
                if CLA.questionOne(test) == 50:
                    numberCorrect += 1
                    answer.append("Replace stick {} in with stick {} in".format(sticks[i], n))
        print("\n".join(answer) if numberCorrect > 0 else "No Answer")

    @staticmethod
    def questionThreeAndFour():
        answers = 0
        sticks = range(1,10)
        combos = [sorted(i) for i in [*perm(sticks, 5)]]
        a=[]
        for bag in combos:
            if bag not in a and CLA.questionOne(bag) == 0:
                answers += 1
                a.append(bag)
                print("The bag could contain sticks with the lengths of " + " in, ".join(map(str,bag))+" in")
        if answers == 0:
            print("No Answer")
print("Answer to question 1:")
print("{}% chance\n".format(CLA.questionOne([1, 3, 5, 7, 9])))
print("Answer to question 2:")
CLA.questionTwo()
print("\nAnswers to questions 3&4:")
CLA.questionThreeAndFour()