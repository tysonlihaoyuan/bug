import requests
from bs4 import BeautifulSoup
import time
import json
import csv
import os
from pandas import*

def digData():
    login_url = 'https://app.axya.co/api/v1/login/'
    checkemail_url="https://app.axya.co/api/v1/checkUserEmail/"
    user_url ="https://app.axya.co/api/v1/company/user/"
    check_email_code="https://app.axya.co/api/v1/login/code/"
    getBuyer_url="https://app.axya.co/_next/data/Vmfu08oe_-eTMtqKGdeUG/en/search/buyers.json"
    getBuyer_url_number="https://app.axya.co/_next/data/Vmfu08oe_-eTMtqKGdeUG/en/search/buyers.json?page="
    searchBuyer_url="https://app.axya.co/api/v1/buyersDiscovery/"
    loginCredential ={
            'email': "lihaoyuan0531@hotmail.com",
            'password':'Tyson0531!'
    }

    emailCredential = {
        'email': "lihaoyuan0531@hotmail.com"
        }
    #current time
    now_time = str(int(time.time()*1000))
    # print (now_time)

    hearderLoginPage={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 
            'Cookie' : '_gid=GA1.2.726019903.1701402999; __Host-next-auth.csrf-token=a9857435c0691e23d89cb5b6236f366ec854a97e77c24612610d723a1e4ae177%7C17252dc7741d57b31041296245a36c5db5771f8c5c0bd9e5412afaff2f8beb6a; __Secure-next-auth.callback-url=https%3A%2F%2Faxya.co; _hjSessionUser_3495031=eyJpZCI6Ijk1NjIxODhkLTUwNGEtNTcwZC05ODBlLWFhMTcxOTIzMjVlYiIsImNyZWF0ZWQiOjE3MDE0MDgyMTk5MDcsImV4aXN0aW5nIjp0cnVlfQ==; amp_abb530=gKgSa9iGMCpB0S4g8zU9F9...1hgjcqa1e.1hgjdq52s.d.0.d; _gat=1; _ga_NMV5V64W60=GS1.1.1701458029.4.1.1701459072.0.0.0; _ga=GA1.1.98368689.1701402999',
            'Accept-Encoding': 'gzip, deflate', 
            'Accept': '*/*',
            'Connection': 'keep-alive'}

    headerLogin={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 
                'Cookie' : 'amp_abb530=IiDxm9mhfqPs2ugAeO7aD2...1hgk3g7hc.1hgk3g7hc.0.0.0; _gid=GA1.2.646015073.1701481816; _gat=1; _ga_NMV5V64W60=GS1.1.1701481816.1.0.1701481816.0.0.0; _ga=GA1.1.361251410.1701481816'
        }
    with requests.session() as s:
        responseLoginPage = s.get(url='https://app.axya.co/auth/login',headers=hearderLoginPage)
        # print(response.request.headers)
        responseLogin=s.post(url=login_url,json=loginCredential,headers=headerLogin)

        login_ephemeral_token=responseLogin.json()["ephemeral_token"]
        login_ephemeral_method=responseLogin.json()["email"]

        email_code = input("please check your email and enter the code")

        verification = {
            "code" : str(email_code),
            "ephemeral_token": str(login_ephemeral_token)
        }

        responseLoginAfterCode  =s.post(url=check_email_code,json=verification,headers=headerLogin)






        # print(responseLogin.request.headers)
        # print (responseLogin.content)
        #get auth token
        token = responseLoginAfterCode.json()["token"]
        authToken = 'JWT {}'.format(token)
        print('JWT {}'.format(token))
        responseCheckEmail=s.post(url=checkemail_url,json=emailCredential,headers=headerLogin)

        hearderAuth={   
                    'authority':'app.axya.co',
                    'method':'GET',
                    'path':'/api/v1/company/user/',
                    'scheme':'https',
                    'Accept' : 'application/json, text/plain, */*',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language':'en',
                    'Authorization':authToken,
                    'Connection': 'keep-alive',
                    'Cookie':'_gid=GA1.2.646015073.1701481816; _gat=1; _ga_NMV5V64W60=GS1.1.1701481816.1.0.1701481816.0.0.0; _ga=GA1.1.361251410.1701481816; amp_abb530=IiDxm9mhfqPs2ugAeO7aD2...1hgk3g7hc.1hgk3gfaq.1.0.1',            
                    'Referer' : 'https://app.axya.co/',
                    'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                    'Sec-Ch-Ua-Mobile': '?0',
                    'Sec-Ch-Ua-Platform' : "Windows",
                    'Sec-Fetch-Dest':'empty',
                    'Sec-Fetch-Mode':'cors',
                    'Sec-Fetch-Site':'same-origin',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
                    }
        #check if the auth is passed
        requestCheckUser= s.get(url=user_url,headers=hearderAuth) 
        print(requestCheckUser.content)
        soup=BeautifulSoup(requestCheckUser.content,"html.parser")
        print(soup.prettify())

        # get all the Buyers 
        responseBuyers=s.get(getBuyer_url)

        # print(responseBuyers.text)
        buyersData = json.loads(responseBuyers.text)
        #print(buyersData)
        companiesResultBuyer=buyersData['pageProps']['results']

        companiesDetailBuyer=[]
        formateCompanies_buyer(companiesResultBuyer,companiesDetailBuyer)
        # for i in range (2,59):
        for i in range (2,4):
            print(i)
            targetUrl = getBuyer_url_number+str(i)
            
            responseBuyers_number=s.get(targetUrl)
            buyersData_number= json.loads(responseBuyers_number.text)
            companiesResultBuyer_number=buyersData_number['pageProps']['results']
            formateCompanies_buyer(companiesResultBuyer_number,companiesDetailBuyer)
        fieldsIds = ['id','name']
        fieldsFinal=['id','name','phone_number','website','email','country','city','street']
        fileName_Buyer="buyer.csv"
        fileName_Buyer_final="buyerFinal.csv"  
        writeToCSV(fieldsIds,fileName_Buyer,companiesDetailBuyer)
    
        finalResult =getFinalResult(searchBuyer_url,hearderAuth)
        writeToCSV(fieldsFinal,fileName_Buyer_final,finalResult)

def getFinalResult(searchBuyer_url,hearderAuth):
    buyers_csv=read_csv("buyer.csv")
    buyersIds=buyers_csv['id'].tolist()
    result = []
    for id in buyersIds:
        searchBuyers_url_target=searchBuyer_url+str(id)
        buyers_search_response=requests.get(url=searchBuyers_url_target,headers=hearderAuth)

        buyers_search_data = json.loads(buyers_search_response.text)

        tempdic={}
        tempdic['id']=buyers_search_data.get('id')
        tempdic['name']=buyers_search_data.get('name')
        tempdic['phone_number']=buyers_search_data.get('phone_number')
        tempdic['website']=buyers_search_data.get('website')
        tempdic['email']=buyers_search_data.get('email')
        tempdic['country']=buyers_search_data['address'].get('country')
        tempdic['city']=buyers_search_data['address'].get('city')
        tempdic['street']=buyers_search_data['address'].get('street')
        result.append(tempdic)
    return result

def formateCompanies_buyer(companiesResult,companiesDetail):
        for company in companiesResult:
            id =company.get('id')
            name=company.get('company').get('name')
            # country=company.get('company').get('country')
            # city=company.get('company').get('city')
            # street=company.get('company').get('street')
            # postcode = company.get('company').get('postal_code')
        

            tempDic={}
            tempDic['id']=company.get('id')
            tempDic['name']=company.get('company').get('name')

            companiesDetail.append(tempDic)

def writeToCSV(fields,fileName,content):
    
    with open(fileName,'w', newline='', encoding="utf-8")as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)  
            
        # writing headers (field names)  
        writer.writeheader()  
            
        # writing data rows  
        writer.writerows(content)
        print("done")  
def main():
    digData()

if __name__ == "__main__":
    main()