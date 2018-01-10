ent1=input("input a number");
ent2=input("input a number");
ent3=input("input a number");
if ent1>ent2 and ent2>=ent3:
  print("ent1 largest")
elif ent2>ent1 and ent1>=ent3:
  print("ent2 is largest")
elif ent3>ent2 and ent2>=ent1:
  print("ent3 is largest")
elif ent3==ent2 and ent2==ent1:
  print("no largest")
