def sumsquare(list):
  flist=[];
  odd=0;
  even=0;
  for num in list:
    if num%2==0:
        even=even + num*num;
    else: 
        odd=odd+num*num;
  flist.append(odd);
  flist.append(even);
  return flist;
