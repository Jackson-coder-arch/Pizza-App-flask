from flask_wtf import FlaskForm
from wtforms.validators import Required, Email, EqualTo
from wtforms import Form, StringField,SubmitField
# from wtforms import StringField, PasswordField, SubmitField, BooleanField
# from wtforms import ValidationError
from wtforms import SelectField,IntegerField


class OrderForm(FlaskForm):
    email = StringField('Enter email to recieve reciept', validators=[Required(), Email()] )
    flavor= SelectField('Pizza Type',choices=[('Hawaiian'),('Pepperoni'),('BBQ-chicken'),('Buffalo'),('Margherita')],validators=[Required()])
    crust =SelectField('Crust', choose=[('Stuffed'),('Thick'),('Cripsy'),('Gluten')])
    size = SelectField('Choose Pizza size', choices = [('Large'), ('Medium'), ('Small')],validators=[Required()])    
    toppings = SelectField('Choose toppings', choices = [('onions'),('Mushroom'),('Cheese'),('Radichio'),('Bacon')],validators=[Required()])
    no_of_pizzas = IntegerField('Enter number of pizzas', validators=[Required()])
    delivery = SelectField('Choose',option=[('Delivery'),('Collection')],validators=[Required()] )
    submit = SubmitField('Order Now')
    

