from collections import namedtuple
from wtforms import Form, FieldList, BooleanField, HiddenField, FormField
from webob.multidict import MultiDict

SandwichItem= namedtuple('SandwichItem', ['item_id', 'want', 'name'])

class SandwichItemForm(Form):
	item_id = HiddenField()
	want = BooleanField()

class SandwichListForm(Form):
	def __init__(self, *args, **kwargs):
		super(SandwichListForm, self).__init__(*args, **kwargs)

		#custom labels on the list's checkboxes
		for item_form in self.items:
			for item in kwargs['data']['items']:
				if item.item_id == item_form.item_id.data:
					item_form.want.label =''
					item_form.label = item.name
	
	items = FieldList(FormField(SandwichItemForm))

item1 = SandwichItem(1, True, 'bread')
item2 = SandwichItem(2, False, 'shitty things')

data = {'items': [item1, item2]}

form = SandwichListForm(data=MultiDict(data))

return form
