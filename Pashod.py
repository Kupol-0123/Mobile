from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

expenses = {}
total_expense = 0

class ExpenseApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        category_label = Label(text="Категория:")
        layout.add_widget(category_label)
        
        self.category_input = TextInput()
        layout.add_widget(self.category_input)
        
        amount_label = Label(text="Сумма:")
        layout.add_widget(amount_label)
        
        self.amount_input = TextInput(input_filter="float")
        layout.add_widget(self.amount_input)
        
        add_button = Button(text="Добавить расход")
        add_button.bind(on_press=self.add_expense)
        layout.add_widget(add_button)
        
        show_button = Button(text="Показать расходы")
        show_button.bind(on_press=self.show_expenses)
        layout.add_widget(show_button)
        
        total_label = Label(text="Общий расход:")
        layout.add_widget(total_label)
        
        self.total_expense_label = Label()
        layout.add_widget(self.total_expense_label)
        
        self.expense_list = Label()
        layout.add_widget(self.expense_list)
        
        return layout
    
    def add_expense(self, instance):
        category = self.category_input.text
        amount = float(self.amount_input.text) if self.amount_input.text else 0
        
        global total_expense
        total_expense += amount
        
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount
        
        self.category_input.text = ""
        self.amount_input.text = ""
    
    def show_expenses(self, instance):
        expense_text = ""
        for category, total in expenses.items():
            expense_text += f"{category}: {total}\n"
        
        self.expense_list.text = expense_text
        self.total_expense_label.text = str(total_expense)

if __name__ == '__main__':
    ExpenseApp().run()