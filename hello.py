h=1.75
w=80.5
B=w/(h*h)
if B<18.5:
 print(f"B={B:.2f},过轻")
elif B>=18.5 and B<25:
  print(f"B={B:.2f},正常")
elif B>=25 and B<28:
    print(f"B={B:.2f},过重")
elif B>=28 and B<32:
    print(f"B={B:.2f},肥胖")
else:
   print(f"B={B:.2f},严重肥胖") 