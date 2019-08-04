'''
Created on 2019. 7. 27.

@author: 405

HTMl에 들어갈 <form>의 <input>을 관리하는 클래스 정의
'''
from django import forms
from vote.models import Question, Choice
#Question 모델클래스와 연동된 Form 클래스 정의
#모델클래스와 Form클래스를 연동시킬려면 ModelForm클래스를 상속받아야함
class QuestionForm(forms.ModelForm):
    #ModelForm클래스에서는 Meta클래스를 정의함으로써
    #어떤 모델클래스와 연동하는지 어떤 변수값을 사용할것인지 표현
    #모델 클래스틑 필수적으로 메타라는 클래스를 정의해줘야 연동되는 모델클래스 객체를 생성하여 사용자로부터 변수값을 입력받을 수 있다.
    class Meta:
        #model, fields, exclude
        #model : 어떤 모델클래스와 연동했는지 저장하는 변수
        #fields, exclude 중 한개의 변수를 사용해 사용할 변수 정의
        model = Question 
        fields = ['title'] #title변수값을 기입할수있도록 정의
        #pub_date를 제외한 나머지변수를 기입할수 있도록 정의
        #exclude = ['pub_date']

#Choice 모델클래스와 연동된 ChoiceForm 클래스 정의
class ChoiceForm(forms.ModelForm):#ModelForm 기능을 하기 위해서는 ModelForm 을 상속받아야한다.
#q 변수와 name 변수를 접근할 수 있도록 설정
    class Meta:
        model = Choice
        fields = ['q','name']
        #(필요한것들을 입력)
        #exclude = ['votes'] (제외할 것 하나만 입력)






