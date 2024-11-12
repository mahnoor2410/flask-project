from flask import render_template

class user_model:
    def user_add_model(self, form):
        try:
            num1 = float(form.get('number1'))
            num2 = float(form.get('number2'))
            result = num1 + num2
        except (ValueError, TypeError):
            result = "Invalid input. Please enter valid numbers."
        
        # Return the result to the template
        return render_template('index.html', result=result)
   
