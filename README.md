# Crypto Wallet

![](Images/22ROOSE-master768.gif)  
<sub>Illustration for Glenn Harvey</sub>

# Criteria A: Planning

## Problem definition

Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all his transaction using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms Sato to find past transactions or important statistics about the currency. Ms Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics. 

Apart for this requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.

## Proposed Solution

Design statement:
I will to design and make a numerical ledger for a client who is Ms. Sato. The numerical ledger will about Bitcoin and is constructed using the software Python. It will take  ———- to make and will be evaluated according to the criteria ———.

Justify the tools/structure of your solution

## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger display the basic description of the cyrptocurrency selected.
3. The electronic ledger allows to enter, withdraw and record transactions.
4. The electronic ledger database is encrypted, and application usage requires password authentication.
5. The electronic ledger allows to display the number of bitcoin in the wallet with a graph (plotext).
6. The electronic ledger shows the value of the wallet in many currcencies.

# Criteria B: Design

## System Diagram

![](https://github.com/Alsa2/unit-1/blob/main/Images/SystemDiagram.png)

 **Fig. 1** System Diagram

## Flow Diagrams


## Record of Tasks
| Task No 	| Planned Action                            	| Planned Outcome                                                                                             	| Time estimate 	| Target completion date 	| Criterion 	|
|---------	|-------------------------------------------	|-------------------------------------------------------------------------------------------------------------	|---------------	|------------------------	|-----------	|
| 1       	| Interview with the Client                 	| To discuss client's needs and define success criteria                                                       	| 10min         	|                        	| A         	|
| 2       	| Create system diagram                     	| To have a clear idea of the hardware and software requirements for the proposed solution                    	| 10min         	| Sep 24                 	| B         	|
| 3       	| Flow diagram login                        	| Created a flow diagram for the login system                                                                 	| 10min         	| Sep 27                 	| B         	|
| 4       	| Login Code                                	| Created the login code                                                                                      	| 40min         	| Sep 27                 	| C         	|
| 5       	| Tested Login System                       	| Tested the login system → Successful                                                                        	| 10min         	| Sep 27                 	| B         	|
| 6       	| Integrating database in login system      	| The login system is capable of interacting with the database                                                	| 20min         	| Sep 28                 	| C         	|
| 7       	| Testing Integrated Database System        	| Tested the login system → Successful                                                                        	| 5min          	| Sep 28                 	| B         	|
| 8       	| Added UI for the login system             	| Have an intuitive and stylish login system                                                                  	| 30min         	| Oct 1                  	| C         	|
| 9       	| Tested UI                                 	| Working and beautiful                                                                                       	| 5min          	| Oct 1                  	| B         	|
| 10      	| Fernet Full Database Encryption           	| The database is fully encrypted for the client privacy                                                      	| 30min         	| Oct 2                  	| C         	|
| 11      	| Tested Encryption                         	| The encryption is working (but the codes are long to enter)                                                 	| 5min          	| Oct 2                  	| B         	|
| 12      	| Default key                               	| Avoid entering key every time (will be removed for the client)                                              	| 15min         	| Oct 3                  	| C         	|
| 13      	| Tested Default key                        	| Tested the default decryption system → Successful                                                           	| 2min          	| Oct 3                  	| B         	|
| 14      	| UI for the Encryption System              	| Make the decryption software intuitive for the user (steps showed for user debugging)                       	| 30min         	| Oct 4                  	| C         	|
| 15      	| Tested UI for Decryption                  	| The animations are sick, UI intuitive for the user → Successful                                             	| 10min         	| Oct 4                  	| B         	|
| 16      	| Database Decryption                       	| Remixed the decryption to do the opposite (Including UI and default key)                                    	| 20min         	| Oct 4                  	| C         	|
| 17      	| Tested Decryption                         	| Tested the decryption system → Successful                                                                   	| 5min          	| Oct 4                  	| B         	|
| 18      	| Debug Menu                                	| Added a hidden debug menu to jump directly to where the developer want (will be removed)                    	| 15min         	| Oct 4                  	| C         	|
| 19      	| Tested Debug Menu                         	| It's properly accessible and working                                                                        	| 5min          	| Oct 4                  	| B         	|
| 20      	| Added the menu travelling tool            	| Menu intuitive to the user and efficient                                                                    	| 30min         	| Oct 5                  	| C         	|
| 21      	| Testing Menu                              	| The menu is working properly                                                                                	| 3min          	| Oct 5                  	| B         	|
| 22      	| Added Transaction edit                    	| Added the add/view/edit/remove transaction system                                                           	| 3h            	| Oct 5                  	| C         	|
| 23      	| Transaction Testing                       	| Interacting as planned with the database, intuitive and efficient                                           	| 10min         	| Oct 5                  	| B         	|
| 24      	| Previous Transaction view                 	| Graph that can show intuitively, a graph with the earnings                                                  	| 45min         	| Oct 6                  	| C         	|
| 25      	| Testing Graph                             	| The graph is intuitive, pleasant to view and most essentially working                                       	| 10min         	| Oct 6                  	| B         	|
| 26      	| Added crypto ⇾ currency graph             	| Added a function in the menu to show a graph of the desired value to value for the desired time             	| 1h            	| Oct 6                  	| C         	|
| 27      	| Tested currency value                     	| Beautiful candlestick, working and easy to use                                                              	| 10min         	| Oct 6                  	| B         	|
| 28      	| Settings menu                             	| Change the color theme, change the password of the user, erase everything...                                	| 40min         	| Oct 7                  	| C         	|
| 29      	| Tested the settings menu                  	| Everything working properly                                                                                 	| 10min         	| Oct 7                  	| B         	|
| 30      	| Class Beta Testing                        	| They reported that the graphics are very intuitive and everything is clear, except for the transaction edit 	| 20min         	| Oct 8                  	| A         	|
| 31      	| House Beta Testing                        	| Reported that all is very clear, intuitive and functional                                                   	| 20min         	| Oct 8                  	| A         	|
| 32      	| Clean up of useless file                  	| Removed all the temps files                                                                                 	| 10min         	| Oct 9                  	| C         	|
| 33      	| Checking that everything is still working 	| Yep everything is still working                                                                             	| 40min         	| Oct 9                  	| B         	|