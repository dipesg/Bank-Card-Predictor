from django.shortcuts import render, redirect
import pandas as pd
import pickle

def index_func(request):
    res = 0
    if request.method == 'POST':
        attrite = request.POST['attrite']
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender'] # select
        children = request.POST['children']
        edu= request.POST['edu'] # select
        marital = request.POST['marital'] # select
        income = request.POST['income'] # select
        monthOnBooks = request.POST['monthOnBooks']
        totalRelationshipCount = request.POST['totalRelationshipCount']
        monthsInactive12mon = request.POST['monthsInactive12mon']
        contactsCount12mon = request.POST['contactsCount12mon']
        creditLimit = request.POST['creditLimit']
        totalRevolvingBal = request.POST['totalRevolvingBal']
        avgOpenToBuy = request.POST['avgOpenToBuy']
        totalAmtChngQ4Q1 = request.POST['totalAmtChngQ4Q1']
        totalTransAmt = request.POST['totalTransAmt']
        totalTransCt = request.POST['totalTransCt']
        totalCtChngQ4Q1= request.POST['totalCtChngQ4Q1']
        avgUtilizationRatio = request.POST['avgUtilizationRatio']

        if name != "":
            df = pd.DataFrame(columns=['Attrition_Flag', 'Customer_Age', 'Gender',
                                       'Dependent_count', 'Education_Level', 'Marital_Status',
                                       'Income_Category', 'Months_on_book',
                                       'Total_Relationship_Count', 'Months_Inactive_12_mon',
                                       'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal',
                                       'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt',
                                       'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio'])

            df2 = {'Attrition_Flag': int(attrite), 'Customer_Age': float(age), 'Gender': int(gender),
                   'Dependent_count': float(children), 'Education_Level': int(edu), 'Marital_Status':
                    int(marital), 'Income_Category': int(income), 'Months_on_book': int(monthOnBooks),
                    'Total_Relationship_Count': int(totalRelationshipCount), 'Months_Inactive_12_mon':
                    int(monthsInactive12mon), 'Contacts_Count_12_mon': int(contactsCount12mon),
                   'Credit_Limit': float(creditLimit), 'Total_Revolving_Bal': float(totalRevolvingBal),
                    'Avg_Open_To_Buy': float(avgOpenToBuy), 'Total_Amt_Chng_Q4_Q1': float(totalAmtChngQ4Q1),
                   'Total_Trans_Amt': float(totalTransAmt), 'Total_Trans_Ct': float(totalTransCt),
                   'Total_Ct_Chng_Q4_Q1': float(totalCtChngQ4Q1), 'Avg_Utilization_Ratio': float(avgUtilizationRatio)}

            df = df.append(df2, ignore_index=True)
            # load the model from disk
            filename = 'polls/BankCardsPCA.pickle'
            pca = pickle.load(open(filename, 'rb'))
            data = pca.transform(df)
            filename1 = 'polls/BankCards.pickle'
            loaded_model = pickle.load(open(filename1, 'rb'))

            res = loaded_model.predict(data)
            print(res)

        else:
            return redirect('homepage')
    else:
        pass

    return render(request, "index.html", {'response': res})
