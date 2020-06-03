from django.shortcuts import render
from django.http import HttpResponse
from .forms import Prediction
from .models import Person_Input

def index(request):
    return render(request, 'home.html')

def calculator(request):
    if request.method == 'POST':
        pred = Prediction(request.POST)
        if pred.is_valid():
            person = pred.save(commit=False)
            indexes = list()
            cancer_sum = person.brother_prostate + person.sister_prostate

            if (person.dark_skin):
                indexes.append(1.2)
            else:
                indexes.append(1)

            if (person.past_cancer):
                indexes.append(1.1)
                cancer_sum += 1
            else:
                indexes.append(1)

            if (person.past_breast_cancer):
                indexes.append(2)
            else:
                indexes.append(1)

            if (person.past_other_cancer):
                indexes.append(1.2)
            else:
                indexes.append(1)

            if (person.father_prostate):
                indexes.append(1.2)
                cancer_sum += 1
            else:
                indexes.append(1)

            if (person.mother_breast):
                indexes.append(1.2)
                cancer_sum += 1
            else:
                indexes.append(1)    

            if (person.brother_prostate == 0):
                indexes.append(1) 
            elif (person.brother_prostate == 1):
                indexes.append(1.2)
            else:
                indexes.append(2)

            if (person.sister_prostate == 0):
                indexes.append(1) 
            elif (person.sister_prostate == 1):
                indexes.append(1.2)
            else:
                indexes.append(2)

            if (person.mutation):
                indexes.append(2)
            else:
                indexes.append(1)
            
            genetic_max = max(indexes)
            person.psa_density = person.psa/person.volume_prostate
            andro_max = 1

            andro_indexes = list()
            imc = 100*person.weight/(person.height**2)

            if (imc>30):
                andro_indexes.append(1.2)
            else:
                andro_indexes.append(1)

            if (person.low_testosterone):
                andro_indexes.append(1.3)
            else:
                andro_indexes.append(1)

            if (person.sexual_difficulties):
                andro_indexes.append(1.1)
            else:
                andro_indexes.append(1)

            if (person.heat):
                andro_indexes.append(1.2)
            else:
                andro_indexes.append(1)

            if (person.medicine_fin_dist):
                andro_indexes.append(1.5)
            else:
                andro_indexes.append(1)

            if (person.medicine_erection):
                andro_indexes.append(1.1)
            else:
                andro_indexes.append(1)

            if (person.medicine_cholesterol):
                andro_indexes.append(1.1)
            else:
                andro_indexes.append(1)

            andro_max = max(andro_indexes)

            person.psa_andro_corr = person.psa * andro_max
            person.psa_density_corr = person.psa_andro_corr / person.volume_prostate
            person.genetic_risk = genetic_max
            person.family_pertinence = min([(person.older_brothers + person.older_sisters)/4, 1])
            person.family_info = person.family_pertinence
            person.irm_to_realise = (person.psa_andro_corr>4) or (person.psa_density>0.1) or (genetic_max>1.5)

            person.apparente_one = person.brothers + person.sisters + 2
            person.declared_cancers = cancer_sum

            person.general_pop_risk = (0.0007*person.age+(0.000013*(person.age**2)))-0.05 
            person.individual_risk = (0.6+6.6*person.psa_density_corr)*person.general_pop_risk*person.genetic_risk
            person.save()
            return render(request, 'results.html', {'person': person})
        else:
            pred = Prediction()
            return render(request, 'calculator.html', {'pred': pred})
    else:
        pred = Prediction()
        return render(request, 'calculator.html', {'pred': pred})
