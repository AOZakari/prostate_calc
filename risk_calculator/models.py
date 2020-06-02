from django.db import models

class Person_Input(models.Model):
    age = models.PositiveSmallIntegerField(verbose_name="Quel est votre Age (ans)")
    brothers = models.PositiveSmallIntegerField(verbose_name="Combien avez-vous de frères ")
    sisters = models.PositiveSmallIntegerField(verbose_name="Combien avez-vous de soeurs ")
    older_brothers = models.PositiveSmallIntegerField(verbose_name="Combien avez-vous de frères plus agés que vous")
    older_sisters = models.PositiveSmallIntegerField(verbose_name="Combien avez-vous de soeurs plus agées que vous")

    dark_skin = models.BooleanField(verbose_name="Avez-vous une peau noire (origine africaine ou antillaise)")
    past_cancer = models.BooleanField(verbose_name="Avez vous eu un cancer")
    past_breast_cancer = models.BooleanField(verbose_name="Avez vous eu un cancer du sein")
    past_other_cancer = models.BooleanField(verbose_name="Avez-vous eu personnellement un des cancers suivants (Colon ou rectum, melanome, cerveau, estomac)")
    father_prostate = models.BooleanField(verbose_name="Avez-vous un père qui a eu un cancer de la prostate")
    mother_breast = models.BooleanField(verbose_name="Avez-vous un mère qui a eu un cancer du sein")

    brother_prostate =  models.PositiveSmallIntegerField(verbose_name="Combien de vos frères ont eu un cancer de la prostate")
    sister_prostate =  models.PositiveSmallIntegerField(verbose_name="Combien de vos soeurs ont eu un cancer du sein")

    mutation = models.BooleanField(verbose_name="Avez-vous une mutation qui prédispose aux cancers Sein (BRCA1 ou BRCA2, Autres)")

    psa =  models.FloatField(verbose_name="Quel est votre taux de PSA (ng/ml)")
    volume_prostate = models.FloatField(verbose_name="Quel est votre volume de prostate (cc mesuré en échographie)")

    weight = models.FloatField(verbose_name="Quels est votre Poids (kg)")
    height = models.FloatField(verbose_name="Quel est votre Taille (cm)")

    low_testosterone = models.BooleanField(verbose_name="Votre taux sanguin de testostérone biodisponible est il <0,3 ng/ml")
    sexual_difficulties = models.BooleanField(verbose_name="Avez vous des difficultés sexuels (baisse de la libido ou des difficultés pour avoir des érections satisfaisantes)")
    heat = models.BooleanField(verbose_name="Avez vous des bouffées de chaleur")
    medicine_fin_dist = models.BooleanField(verbose_name="Prenez vous un des médicaments suivant (Finasteride ou Dutasteride)")
    medicine_erection = models.BooleanField(verbose_name="Prenez vous un des médicaments pour faciliter les érections?")
    medicine_cholesterol = models.BooleanField(verbose_name="Avez-vous un traitement pour réduire votre taux de cholestérol?")

    psa_andro_corr = models.FloatField(verbose_name="PSA corrigé Andropause")
    psa_density = models.FloatField(verbose_name="PSA densité")
    psa_density_corr = models.FloatField(verbose_name="PSA densité corrigé")
    genetic_risk = models.FloatField(verbose_name="Risque génétique")
    family_pertinence = models.FloatField(verbose_name="Pertinence familiale")
    family_info = models.FloatField(verbose_name="Informativité familiale")

    irm_to_realise = models.BooleanField(verbose_name="IRM prostatique à réaliser")
    
    general_pop_risk = models.FloatField()
    individual_risk = models.FloatField()

    apparente_one = models.PositiveSmallIntegerField()
    declared_cancers = models.PositiveSmallIntegerField()