import string
fr = open('NYSE.txt', 'r');
fw = open('ticker.txt','w');
count=0;
#get rid of subject line
temp_line=fr.readline();
temp_line=fr.readline();

while temp_line!="":
    line_arr = temp_line.split( );
    ticker=line_arr[0];
    if '.' not in ticker:
        if '-' not in ticker:
            fw.write(ticker);
            fw.write('\n');
            count=count+1;
    
    temp_line=fr.readline();

print("file cleaning finished.");
print("valid ticker count is "+str(count));
fr.close();
fw.close();
