from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit

class GuessPokemon(forms.Form):
    base_HP = forms.IntegerField()
    attack = forms.IntegerField()
    defense = forms.IntegerField()
    special_attack = forms.IntegerField()
    special_defense = forms.IntegerField()
    speed = forms.IntegerField()
    generation = forms.IntegerField()
    legendary = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper  # some crispy tags.
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'base_HP',
            'attack', 'defense',
            'special_attack', 'special_defense',
            'speed',
            'generation',
            'legendary',

            Submit('submit', 'Submit', css_class='btn-success'),
        )


class PokeSearch(forms.Form):
    number = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper  # some crispy tags.
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'number',

            Submit('submit', 'Submit', css_class='btn-success'),
        )

class PokeSearchByName(forms.Form):

    pokemon_name = forms.CharField(max_length=20)
