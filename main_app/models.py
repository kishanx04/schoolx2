from main_app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(20),unique=True,nullable=False)
	email = db.Column(db.String(120),unique=True,nullable=False)
	password = db.Column(db.String(60),nullable=False)
	image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
	id_type_user = db.Integer, db.ForeignKey('id_type_user')
	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Notice(db.Model):
	"""docstring for Notice"""
	id_title = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(20),unique=True,nullable=False)
	description = db.Column(db.Text(250),unique=True,nullable=False)
	image = db.Column(db.String(20),nullable=False,default='default.jpg')
	date_of_post = db.Column(db.DateTime(),unique=True,nullable=False)
	post_by = db.Column(db.Integer,unique=True,nullable=False)
	
	def __repr__(self):
		return f"User('{self.title}', '{self.description}', '{self.image_file}', '{self.date_of_post}')"

class Adress(db.Model):
	"""docstring for Adress"""
	id_adress = db.Column(db.Integer,primary_key=True)
	street = db.Column(db.String(20),unique=True,nullable=False)
	district = db.Column(db.String(20),unique=True,nullable=False)
	post_office = db.Column(db.String(20),unique=True,nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
	
	def __repr__(self):
		return f"adress('{self.street}', '{self.district}', '{self.post_office}')"

class Fees(db.Model):
	"""docstring for fees"""
	id_fee = db.Column(db.Integer,primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
	tuition_fee = db.Column(db.Integer,unique=True,nullable=False)
	transport_fee = db.Column(db.Integer,unique=True,nullable=False)
	total_monthly_fee = db.Column(db.Integer,unique=True,nullable=False)
	
class Students(db.Model):
	"""docstring for fees"""
	id_student = db.Column(db.Integer,primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
	
	father_name = db.Column(db.String(20),unique=True,nullable=False)
	mother_name = db.Column(db.String(20),unique=True,nullable=False)
	phone_number = db.Column(db.String(20),unique=True,nullable=False)
	birth_certificate_no = db.Column(db.Integer,unique=True,nullable=False)
	date_of_admition = db.Column(db.DateTime(),unique=True,nullable=False)



class Type_user(db.Model):
	id_type_user = db.Column(db.Integer,primary_key=True)
	desc = db.Column(db.String(20),unique=True,nullable=False)
	name = db.Column(db.String(20),unique=True,nullable=False)