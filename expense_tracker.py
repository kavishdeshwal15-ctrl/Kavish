# my expense tracker assignment
MY_LIST = [] 

def getNUM():
    while 1:
        i=input("Amt (Rs): ").strip()
        # check if it is a number
        safe_check = i.replace('.', '', 1)
        if safe_check.isdigit() and len(safe_check)>0:
            num_z=float(i)
            if num_z>0: return num_z
            else: print("needs to be >0")
        else:     
            print("enter proper num")

def DATE_ask():
    while 1:
        userD=input("Date YYYY-MM-DD: ")
        # manual check date
        p = userD.split('-')
        if len(p)==3 and len(p[0])==4:
            return userD
        else: print("format missing")


def ADDstuff():
    print("\n*add it*")
    v = getNUM()
    c = input("Cat: ")
    if c=="": c="misc"
    
    mx=0
    for ele in MY_LIST:
        if ele['ID']>mx: mx=ele['ID']
    newID = mx+1
    
    my_dict = {'ID':newID,'amt':v,'catG':c.title(),'dt':DATE_ask()}
    MY_LIST.append(my_dict)
    print("done!")

def showing_everything():
    if len(MY_LIST)==0: 
        print("empty.."); return
    totSum = 0
    for i in range(len(MY_LIST)):
        o = MY_LIST[i]
        x = "Rs.%s" % round(o['amt'],2)
        print("id:%s  date:%s  cat:%s  val:%s" % (o['ID'], o['dt'], o['catG'], x))
        totSum+=o['amt']
    print("total spent =",totSum)

def PrintByC():
    listC=[]
    # getting all unique cats
    for a in MY_LIST:
        if a['catG'] not in listC: listC.append(a['catG'])
    print("Available Cats::", listC)

    which=input("which cat to show? ").lower()
    sub=0; got1=0
    for q in MY_LIST:
        if q['catG'].lower()==which:
            print("found: Rs.%s on %s" % (q['amt'], q['dt']))
            sub+=q['amt']; got1=1
    if got1==0: print("None!")
    else: print("SubT=", sub)

def SUMMARY_go():
    if len(MY_LIST)==0: return
    t1=0; D2={}
    maxval=MY_LIST[0]
    for itm in MY_LIST:
        t1+=itm['amt']
        k=itm['catG']
        if k not in D2: D2[k]=0
        D2[k]+=itm['amt']
        if itm['amt']>maxval['amt']: maxval=itm

    print("Expense sum!! Rs.%s" % t1)
    for KK in D2:
        print("-> %s = Rs.%s" % (KK, D2[KK]))
    print("Highest is Rs.%s (%s)" % (maxval['amt'], maxval['catG']))

def del1():
    showing_everything()
    target_str = input("del id (0=cancel): ").strip()
    
    if target_str.isdigit()==False:
        print("invalid input")
        return
        
    targetID = int(target_str)
    if targetID==0: return

    for index in range(len(MY_LIST)):
        if MY_LIST[index]['ID']==targetID:
            ans = input("del actual expense? y/n > ")
            if ans=='y':
                MY_LIST.pop(index)
                print("deleted bro")
            return
    print("not found id")

print("--- SPEND TRACK ---")

# main loop without function wrapper
while 1:
    print("\n1:Add 2:All 3:Cat 4:Sum 5:Del 6:Quit")
    O=input("? ").strip()
    
    if O=='1': ADDstuff()
    elif O=='2': showing_everything()
    elif O=='3': PrintByC()
    elif O=='4': SUMMARY_go()
    elif O=='5': del1()
    elif O=='6': 
        print("bye")
        break
    else: print("err")
