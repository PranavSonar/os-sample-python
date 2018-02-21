from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    import json
    import requests
    import os
    import sys
    from bs4 import BeautifulSoup
    import requests
    from datetime import datetime
    from pytz import timezone
        
    h_d=5
    h_send=0 #h_send?
    b_1=0
    t_1=0
    sl_1=0
    f_o=2
    cycle=0
    h1_send=0
    h2_send=0
    h3_send=0
    h4_send=0
    h5_send=0
    h6_send=0
    h7_send=0
    h8_send=0
    t_2=0
    t_3=0
    t_4=0
    t_5=0
    t_6=0
    t_7=0
    t_8=0
    t_1=0
    sl_1=0
    sl_2=0
    sl_3=0
    sl_4=0
    sl_5=0
    sl_6=0
    sl_7=0
    sl_8=0
    b_1=0
    b_2=0
    b_3=0
    b_4=0
    b_5=0
    b_6=0
    b_7=0
    b_8=0
    
    ta_cnt1=ta_cnt2=ta_cnt3=ta_cnt4=ta_cnt5=ta_cnt6=ta_cnt7=ta_cnt8=ta_cnt9=0
    
    line_sep='-----------------------------------------------------------------------'
    day_sep='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    format = "%Y-%m-%d %H:%M:%S"
    def get_time():
        # Convert to Asia/Kolkata time zone
        now_utc = datetime.now(timezone('UTC'))
        now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
        return now_asia.strftime(format)
        #Output: 2015-05-18 15:32:47 IST+0530
    
    file = open("test_10_10.txt", "a")
    file.write(day_sep+'\n') 
    #file.write(line_sep+'\n') 
    while 1:
        ticker='CRUDE'
        url_dict = {'GAZP' : 'https://www.investing.com/equities/gazprom?cid=32732',
                'LKOD' : 'https://www.investing.com/equities/nk-lukoil-oao?cid=48436', 
                'ROSN' : 'https://www.investing.com/equities/rosneft?cid=48483',
                'NVTK' : 'https://www.investing.com/equities/novatek-gdr?cid=48475',
                'SGGD' : 'https://www.investing.com/equities/surgutneftegaz?cid=48477',
                'USDRUB' : 'https://www.investing.com/currencies/usd-rub',
                'LCO' : 'https://www.investing.com/commodities/brent-oil',
                'EU50' : 'https://www.investing.com/indices/eu-stoxx50',
                'USDNOK' : 'https://www.investing.com/currencies/usd-nok',
                'EURUSD' : 'https://www.investing.com/currencies/eur-usd',
                'OBX' : 'https://www.investing.com/indices/oslo-obx',
                'BHP' : 'https://www.investing.com/equities/bhp-billiton-ltd-nyse-exch',
                'MNOD' : 'https://www.investing.com/equities/jsc-mmc-norilsk-nickel?cid=48470',
                'PL1' : 'https://www.investing.com/commodities/platinum',
                'RSX' : 'https://www.investing.com/etfs/marketvectors-tr-russia',
                'RTS' : 'https://www.investing.com/indices/rtsi',
                'CLR' : 'https://www.investing.com/equities/continental-resources-inc',
                'DVN' : 'https://www.investing.com/equities/devon-energy', 
                'MRO' : 'https://www.investing.com/equities/marathon-oil',
                'EOG' : 'https://www.investing.com/equities/eog-resources',
                'WLL' : 'https://www.investing.com/equities/whiting-petroleum-corp', 
                'SM1' : 'https://www.investing.com/indices/switzerland-20',
                'USDCHF' : 'https://www.investing.com/currencies/usd-chf',
                'CHL' : 'https://www.investing.com/equities/china-mobile-limited-exch',
                'T' : 'https://www.investing.com/equities/at-t', 
                'VOD' : 'https://www.investing.com/equities/vodafone-group-plc-exch',
                'AMX' : 'https://www.investing.com/equities/america-movil',
                'SP1' : 'https://www.investing.com/indices/us-spx-500', 
                'IYZ' : 'https://www.investing.com/etfs/ishares-djsu-telecommunications',
                'DM1' : 'https://www.investing.com/indices/us-30-futures',
                'DX1' : 'https://www.investing.com/quotes/us-dollar-index', 
                'UX1' : 'https://www.investing.com/indices/us-spx-vix-futures',
                'EWA' : 'https://www.investing.com/etfs/ishares-msci-australia-index',
                'EWC' : 'https://www.investing.com/etfs/ishares-msci-canada', 
                'AUDCAD' : 'https://www.investing.com/currencies/aud-cad',
                'USDCAD' : 'https://www.investing.com/currencies/usd-cad',
                'AUDUSD' : 'https://www.investing.com/currencies/aud-usd',
                'EZU' : 'https://www.investing.com/etfs/ishares-msci-emu', 
                'EURCAD' : 'https://www.investing.com/currencies/eur-cad',
                'EURUSD' : 'https://www.investing.com/currencies/eur-usd',
                'EWU' : 'https://www.investing.com/etfs/ishares-msci-uk',
                'EURGBP' : 'https://www.investing.com/currencies/eur-gbp',
                'GBPUSD' : 'https://www.investing.com/currencies/gbp-usd',
                'XME' : 'https://www.investing.com/etfs/spdr-s-p-metals---mining',
                'PL1' :  'https://www.investing.com/commodities/platinum',
                'HG12' : 'https://www.investing.com/commodities/copper',
                'CRUDE' : 'https://in.investing.com/commodities/crude-oil-streaming-chart?cid=49774',}
        
        try:
            response = requests.get(url_dict[ticker], headers={"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"})
            soup = BeautifulSoup(response.content, "html.parser")
            value = soup.find('input', {'class':'newInput inputTextBox alertValue'}).get('value')
            investing_price = round(float(value.replace(",", "")), 4)
            resp =  '{} price: {} \n\nDownloaded from {}'.format(ticker, investing_price, url_dict[ticker])
        except KeyError:
            resp =  'Investing.com doesnt contain current prices of {} asset. Please, use other source.'.format(ticker)
        #return resp
        
        price = investing_price
        #file.write(test)
        print price
        
        s=False
        if(cycle==0):
            
            cycle=1
            f_o=0 #first_O
            o_1=price
            t_1=(o_1)+10
            sl_1=(o_1)-10
            start_time = str(get_time())
            t1= ">>buy@"+str(o_1)+'\t\t'+start_time+"\n"
            print t1
            file.write(line_sep+'\n') 
            #file.write('Strat time: \t'+start_time+'\n')
            file.write(t1) 
            
        else:
            pass
            #s_1=price,t_1=s_1-10,sl_1=b_1+10 
        
        
        t1=''
        
        
        #o_2=3195
        o_2=(o_1-h_d)	#3200-5
        t_2=sl_1		#3190
        sl_2=t_1		#3210
        
        
        t_3=t_5=t_7=t_9=t_1
        t_4=t_6=t_8=t_2
        o_3=o_5=o_7=o_9=o_1
        o_4=o_6=o_8=o_2
        sl_3=sl_5=sl_7=sl_9=sl_1
        sl_4=sl_6=sl_8=sl_2
        h1_send=h2_send=h3_send=h4_send=h5_send=h6_send=h7_send=h8_send=h9_send=0
        
        lot_1=1 #1
        lot_2=3 #6
        lot_3=6 #12
        lot_4=12    #34
        lot_5=24    #61
        lot_6=48    #169
        lot_7=96
        lot_8=192
        
        #price=str(price)
        #print f_o;    
             
        if(cycle!=0):
            if(f_o==0):
                
                if(cycle==1):
                    #print 'cycle 1\n'
                    if((price>=t_1) and cycle==1):
                        #sget_time = str(get_time())
                        ta_cnt1 = ta_cnt1+1;
                        t1= '>t_1 complete\t@'+str(price)+' Pts:'+str(lot_1*(price-o_1))+'\t\t'+str(get_time())+'Count: '+ta_cnt1+'\n\n'
                        file.write(t1)
                        print t1
                        cycle=0
                    	#e_b1()#exit
                    elif((price<=o_2 and price>sl_1) and cycle==1 and h1_send==0):			#S	 and price>sl_1
                	    #h_s1
                    	t1= 'cycle 2 started\tSell_@'+str(price)+'\t\t'+str(get_time())+'\n'
                    	file.write(t1)
                    	print t1
                    	#h_s1=(o_1-sl_1)/2;h_t1=sl_1;h_sl1=t_1  #opposite or
                    	h1_send=1
                    	cycle=2
                	elif(price<=sl_1 and cycle==1):
                        t1= '>sl_1 hit\t@'+str(price)+'\t\t'+str(get_time())+'\n\n'
                        print t1
                        file.write(t1)
                	    cycle=0
                    	#e_b1()
                	
                if(cycle==2):
                    if((price<=t_2) and cycle==2):
            		    cycle=0
            		    ta_cnt2 = ta_cnt2+1;
            		    t1= '>t_2 complete\t@'+str(price)+' Pts:'+str((lot_1*(price-o_1))+(lot_2*(o_2-price)))+'\t\t'+str(get_time())+'Count: '+ta_cnt2+'\n\n'
            		    print t1
            		    file.write(t1)
        	        elif((price==o_3 and price<sl_2) and cycle==2 and h2_send==0):	#B
            		    t1= 'cycle 3 started\tBuy_@'+str(price)+'\t\t'+str(get_time())+'\n'
            		    print t1
            		    file.write(t1)
            		    cycle=3
            		    h2_send=1
        	        elif((price>=sl_2) and cycle==2):
            	    	#print 'sl_2 hit'
            		    t1= '>sl_2 hit\t@'+str(price)+'\t\t'+str(get_time())+'\n\n'
            		    print t1
            		    file.write(t1)
            		    cycle=0
            		    #e_b1()
                if(cycle==3):						#b
        	        if((price>=t_3) and cycle==3):
    	                ta_cnt3 = ta_cnt3+1;
    	                t1= '>t_3 successfully\t@'+str(price)+' Pts:'+str((lot_1*(price-o_1))+(lot_2*(o_2-price))+(lot_3*(price-o_3)))+'\t\t'+str(get_time())+'Count: '+ta_cnt3+'\n\n'
    	                file.write(t1)
    	                cycle=0
                		#e_b1()#exit
                    elif((price==o_4 and price>sl_3) and cycle==3 and h3_send==0):			#S	 and price>sl_1
                		#h_s1
                		t1= 'cycle 4 started\tSell@'+str(price)+'\t\t'+str(get_time())+'\n'
                		file.write(t1)
                		#h_s1=(o_1-sl_1)/2;h_t1=sl_1;h_sl1=t_1  #opposite or
                		h3_send=1
                		cycle=4
                    elif(price<=sl_3 and cycle==3):
                		t1= '>sl_3 hit\t@'+str(price)+'\t\t'+str(get_time())+'\n\n'
                		file.write(t1)
                		cycle=0
                if(cycle==4):		#S
                	 if((price<=t_4) and cycle==4):
                		cycle=0
                		ta_cnt4 = ta_cnt4+1;
                		t1= 't_4 complete\t@'+str(price)+' Pts:'+str((lot_1*(price-o_1))+(lot_2*(o_2-price))+(lot_3*(price-o_3))+(lot_4*(o_4-price)))+'\t\t'+str(get_time())+'Count: '+ta_cnt4+'\n\n'
                		file.write(t1)
                     elif((price==o_5 and price<sl_4) and cycle==4 and h4_send==0):	#B
                		t1= 'cycle 5 started\tBuy@'+str(price)+'\t\t'+str(get_time())+'\n'
                		file.write(t1)
                		cycle=5
                		h4_send=1
                     elif((price>=sl_4) and cycle==4):
                		#print 'sl_2 hit'
                		t1= '>sl_4 hit\t@'+str(price)+'\t\t'+str(get_time())+'\n\n'
                		file.write(t1)
                		cycle=0
                if(cycle==5):			#b
            	    if((price>=t_5) and cycle==5):
        	        	ta_cnt5 = ta_cnt5+1;
                		t1= '>t_5 successfully\t@'+str(price)+' Pts:'+str((lot_1*(price-o_1))+(lot_2*(o_2-price))+(lot_3*(price-o_3))+(lot_4*(o_4-price))+(lot_5*(price-o_5)))+'\t\t'+str(get_time())+'Count: '+ta_cnt5+'\n\n'
                		file.write(t1)
                		cycle=0
                		#e_b1()#exit
            	    elif((price==o_6 and price>sl_5) and cycle==5 and h5_send==0):			#S	 and price>sl_1
                		#h_s1
                		t1= 'cycle 6 started\tSell@'+str(price)+'\t\t'+str(get_time())+'\n'
                		file.write(t1)
                		#h_s1=(o_1-sl_1)/2;h_t1=sl_1;h_sl1=t_1  #opposite or
                		h1_send=1
                		cycle=6
            	    elif(price<=sl_5 and cycle==5):
                		t1= '>sl_5 hit\t@'+str(price)+'\t\t'+str(get_time())+'\n\n'
                		file.write(t1)
                		cycle=0
                if(cycle==6):					#S
            	    if((price<=t_6) and cycle==6):
                		cycle=0
                		ta_cnt6 = ta_cnt6+1;
                		t1= '>t_6 complete\t@'+str(price)+' Pts:'+str((lot_1*(price-o_1))+(lot_2*(o_2-price))+(lot_3*(price-o_3))+(lot_4*(o_4-price))+(lot_5*(price-o_5))+(lot_6*(o_6-price)))+'\t\t'+str(get_time())+' Count: '+ta_cnt6+'\n\n'
                		file.write(t1)
            	    elif((price==o_7 and price<sl_6) and cycle==6 and h6_send==0):	#B
                		t1= 'cycle 7 started\tBuy@'+str(price)+'\t\t'+str(get_time())+'\n'
                		file.write(t1)
                		cycle=7
                		h2_send=1
            	    elif((price>=sl_6) and cycle==6):
                		#print 'sl_2 hit'
                		t1= '>sl_6 hit\t@'+str(price)+'\t\t'+str(get_time())+'\n\n'
                		file.write(t1)
                		cycle=0
                if(cycle==7):					#b
            	    if((price>=t_7) and cycle==7):
        	        	ta_cnt7 = ta_cnt7+1;
                		t1= '>t_7 successfully\t@'+str(price)+' Pts:'+str((lot_1*(price-o_1))+(lot_2*(o_2-price))+(lot_3*(price-o_3))+(lot_4*(o_4-price))+(lot_5*(price-o_5))+(lot_6*(o_6-price))+(lot_7*(price-o_7)))+'\t\t'+str(get_time())+' Count: '+ta_cnt7+'\n\n'
                		file.write(t1)
                		cycle=0
                		#e_b1()#exit
            	    elif((price==o_8 and price>sl_7) and cycle==7 and h7_send==0):			#S	 and price>sl_1
                		#h_s1
                		t1= 'cycle 8 started\tSell@'+str(price)+'\t\t'+str(get_time())+'\n'
                		file.write(t1)
                		#h_s1=(o_1-sl_1)/2;h_t1=sl_1;h_sl1=t_1  #opposite or
                		h1_send=1
                		cycle=8
            	    elif(price<=sl_7 and cycle==1):
                		t1= '>sl_7 hit\t@'+str(price)+'\t\t'+str(get_time())+'\n\n'
                		file.write(t1)
                		cycle=0	
                if(cycle==8):									#s
            	    if((price<=t_8) and cycle==8):
                		cycle=0
                		ta_cnt8 = ta_cnt8+1;
                		t1= '>t_8 complete\t@'+str(price)+' Pts:'+str((lot_1*(price-o_1))+(lot_2*(o_2-price))+(lot_3*(price-o_3))+(lot_4*(o_4-price))+(lot_5*(price-o_5))+(lot_6*(o_6-price))+(lot_7*(price-o_7))+(lot_8*(o_8-price)))+'\t\t'+str(get_time())+' Count: '+ta_cnt8+'\n\n'
                		file.write(t1)
            	    elif((price==o_9 and price<sl_8) and cycle==8 and h8_send==0):	#B
                		t1= 'cycle 9 started\t@Buy'+str(price)+'\t\t'+str(get_time())+'\n'
                		file.write(t1)
                		cycle=9
                		h2_send=1
            	    elif((price>=sl_8) and cycle==8):
                		#print 'sl_2 hit'
                		t1= '>sl_8 hit\t@'+str(price)+'\t\t'+str(get_time())+'\n\n'
                		file.write(t1)
                		cycle=0
        		
            elif(f_o==1):
              if(cycle==1):
                 if((price==t_1) and cycle==1):
                    print 'T successfully'
                    #e_b1()#exit
                 elif((price==sl_1) and cycle==1):
                    print 'sl_1 hit'
                    #e_b1()
                 elif((price==(b_1-h_d)) and cycle==1 and h1_send==0):
                    #h_s1
                    h_s1=(b_1+sl_1)/2;h_t1=sl_1;h_sl1=t_1 #opposite or
                    cycle=2
                    h1_send=1
              if(cycle==2):
                 if((price==t_2) and cycle==2):
                    print 't_2 complete'
                    #e_b1()#exit
                 elif((price==sl_2) and cycle==2):
                    print 'sl_2 hit'
                    #e_b1()
                 elif((price==(b_2+h_d)) and cycle==2 and h2_send==0):
                    #h_s2
                    cycle=3
                    h2_send=1
              if(cycle==3):
                 if((price==t_3) and cycle==3):
                    print 't_2 complete'
                    #e_b1()#exit
                 elif((price==sl_3) and cycle==3):
                    print 'sl_3 hit'
                    #e_b1()
                 elif((price==(b_3+h_d)) and cycle==3 and h3_send==0):
                   # h_s3
                    cycle=4
                    h3_send=1
              if(cycle==4):
                 if((price==t_4) and cycle==4):
                    print 't_4 complete'
                    #e_b1()#exit
                 elif((price==sl_4) and cycle==4):
                    print 'sl_4 hit'
                    #e_b1()
                 elif((price==(b_4+h_d)) and cycle==4 and h4_send==0):
                    #h_s2
                    cycle=5
                    h4_send=1
              if(cycle==5):
                 if((price==t_5) and cycle==5):
                    print 't_5 complete'
                    #e_b1()#exit
                 elif((price==sl_5) and cycle==5):
                    print 'sl_5 hit'
                    #e_b1()
                 elif((price==(b_5+h_d)) and cycle==5 and h5_send==0):
                    #h_s5
                    cycle=6
                    h5_send=1
              if(cycle==6):
                 if((price==t_6) and cycle==6):
                    print 't_6 complete'
                    #e_b1()#exit
                 elif((price==sl_6) and cycle==6):
                    print 'sl_6 hit'
                    #e_b1()
                 elif((price==(b_6+h_d)) and cycle==6 and h6_send==0):
                    #h_s6
                    cycle=7
                    h6_send=1
              if(cycle==7):
                 if((price==t_7) and cycle==7):
                    print 't_7 complete'
                    #e_b1()#exit
                 elif((price==sl_7) and cycle==7):
                    print 'sl_7 hit'
                    #e_b1()
                 elif((price==(b_7+h_d)) and cycle==7 and h7_send==0):
                    #h_s7
                    cycle=8
                    h7_send=1
              if(cycle==8):
                 if((price==t_8) and cycle==8):
                    print 't_8 complete'
                    #e_b1()#exit
                 elif((price==sl_8) and cycle==8):
                    print 'sl_8 hit'
                    #e_b1()
                 elif((price==(b_8+h_d)) and cycle==8 and h8_send==0):
                    #h_s8
                    cycle=9
                    h8_send=1
            else:
              pass
        file.flush()


if __name__ == "__main__":
    application.run()
