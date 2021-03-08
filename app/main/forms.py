from flask_wtf import FlaskForm
from wtforms.validators import Required, Email, EqualTo
from wtforms import Form, StringField,SubmitField
# from wtforms import StringField, PasswordField, SubmitField, BooleanField
# from wtforms import ValidationError
from wtforms import SelectField,IntegerField


class OrderForm(FlaskForm):
    email = StringField('Enter email to recieve reciept', validators=[Required(), Email()] )
    flavor= SelectField('Pizza Type',choices=[('Hawaiian','Hawaiian'),('Pepperoni','Pepperoni'),('BBQ-chicken','BBQ-chicken'),('Buffalo','Buffalo'),('Margherita','Margherita')],validators=[Required()])
    crust =SelectField('Crust', choices=[('Stuffed','Stuffed'),('Thick','Thick'),('Cripsy','Cripsy'),('Gluten', 'Gluten')])
    size = SelectField('Choose Pizza size', choices = [('Large','Large'), ('Medium','Medium'), ('Small','Small')],validators=[Required()])    
    toppings = SelectField('Choose toppings', choices = [('Onions','Onions'),('Mushroom','Mushroom'),('Cheese','Cheese'),('Radichio','Radichio'),('Bacon','Bacon')],validators=[Required()])
    no_of_pizzas = IntegerField('Enter number of pizzas', validators=[Required()])
    delivery = SelectField('Choose', choices=[('Delivery','Delivery'),('Collection','Collection')],validators=[Required()] )
    submit = SubmitField('Order Now')
    

