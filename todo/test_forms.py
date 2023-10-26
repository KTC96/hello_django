from django.test import TestCase
from .forms import ItemForm

# Create your tests here.


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})  # simulate no entry
        self.assertFalse(form.is_valid())  # not valid
        # dictionary of fields which were errors and associated error messages
        # If name key is in there
        self.assertIn('name', form.errors.keys())
        # check if the error message in the name field matches
        self.assertEqual(form.errors['name'][0], 'This field is required.')

# check that the done field is not required
    def test_done_field_is_not_required(self):
        # create a form sending just a name and test if valid
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

# ensure the only fields displayed on the form are name and done
    def test_fields_are_explicit_in_form_metaclass(self):
        # Create empty form
        form = ItemForm()
        # check if the form.meta.fields is equal
        # to a list with name and done inside
        self.assertEqual(form.Meta.fields, ['name', 'done'])
