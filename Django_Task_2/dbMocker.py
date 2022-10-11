import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task2.settings')
django.setup()



from taskModel import models



def populateModels():
    for i in range(30,40):
        models.Model.objects.create(model_name=f'model{i}')


if  __name__=='__main__':
    populateModels()
