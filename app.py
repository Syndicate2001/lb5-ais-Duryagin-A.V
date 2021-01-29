from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///duryagin.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class BackupData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    backupdate = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<BackupData %r>' % self.id


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FIO_of_employee = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(100), nullable=False)
    marital_status = db.Column(db.String(100), nullable=False)
    start_of_working_in_department_date = db.Column(db.Integer, nullable=False)
    last_position = db.Column(db.String(100), nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    end_of_working_in_department_date = db.Column(db.Integer, nullable=False)
    position = db.Column(db.Integer, nullable=False)
    department = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return '<Employee %r>' % self.id


class Relocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_of_working_date = db.Column(db.Integer, nullable=False)
    end_of_working_date = db.Column(db.Integer, nullable=False)
    title_of_position = db.Column(db.String(100), nullable=False)



    def __repr__(self):
        return '<Relocation %r>' % self.id


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_department = db.Column(db.String(100), nullable=False)
    head_of_department = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return '<Department %r>' % self.id


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_of_position = db.Column(db.String(100), nullable=False)
    short_title = db.Column(db.String(100), nullable=False)
    cipher = db.Column(db.Integer, nullable=False)
    low_border = db.Column(db.Integer, nullable=False)
    high_border = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Position %r>' % self.id


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_company = db.Column(db.String(100), nullable=False)
    adress_of_company = db.Column(db.String(100), nullable=False)
    head_of_company = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return '<Company %r>' % self.id




@app.route('/backup')
def backup():
    backup = BackupData.query.order_by(BackupData.id.desc()).all()
    return render_template("backup.html", backup=backup)


@app.route('/backup/<int:id>/update', methods=['POST', 'GET'])
def backup_update(id):
    backup = BackupData.query.get(id)
    if request.method == "POST":
        backup.backupdate = request.form['backupdate']

        try:
            db.session.commit()
            return redirect('/backup')
        except:
            return "При радактировании резервных данных произошла ошибка"
    else:
        return render_template("update_backup.html", backup=backup)


@app.route('/create_backup', methods=['GET', 'POST'])
def backup_create():
    if request.method == "POST":
        backupdate = request.form['backupdate']

        backup = BackupData(backupdate=backupdate)

        try:
            db.session.add(backup)
            db.session.commit()
            return redirect('/backup')
        except:
            return "При добавлении резервных данных произошла ошибка"
    else:
        return render_template("create_backup.html")


@app.route('/backup/<int:id>/delete')
def backup_delete(id):
    backup = BackupData.query.get_or_404(id)

    try:
        db.session.delete(backup)
        db.session.commit()
        return redirect('/backup')
    except:
        return "При удалении резеврных данных произошла ошибка"


@app.route('/backup/<int:id>')
def backup_detail(id):
    backup = BackupData.query.get(id)
    return render_template("backup_detail.html", backup=backup)


@app.route('/employee')
def employee():
    employee = Employee.query.order_by(Employee.id.desc()).all()
    return render_template("employee.html", employee=employee)


@app.route('/employee/<int:id>/update', methods=['POST', 'GET'])
def employee_update(id):
    employee = Employee.query.get(id)
    if request.method == "POST":
        employee.FIO_of_employee = request.form['FIO_of_employee']
        employee.age = request.form['age']
        employee.sex = request.form['sex']
        employee.marital_status = request.form['marital_status']
        employee.start_of_working_in_department_date = request.form['start_of_working_in_department_date']
        employee.last_position = request.form['last_position']
        employee.rank = request.form['rank']
        employee.end_of_working_in_department_date = request.form['end_of_working_in_department_date']
        employee.position = request.form['position']
        employee.department = request.form['department']

        try:
            db.session.commit()
            return redirect('/employee')
        except:
            return "При радактировании сотрудника произошла ошибка"
    else:
        return render_template("update_employee.html", employee=employee)


@app.route('/create_employee', methods=['GET', 'POST'])
def employee_create():
    if request.method == "POST":
        FIO_of_employee = request.form['FIO_of_employee']
        age = request.form['age']
        sex = request.form['sex']
        marital_status = request.form['marital_status']
        start_of_working_in_department_date = request.form['start_of_working_in_department_date']
        last_position = request.form['last_position']
        rank = request.form['rank']
        end_of_working_in_department_date = request.form['end_of_working_in_department_date']
        position = request.form['position']
        department = request.form['department']

        employee = Employee(FIO_of_employee=FIO_of_employee, age=age, sex=sex, marital_status=marital_status,
        start_of_working_in_department_date=start_of_working_in_department_date, last_position=last_position, rank=rank,
        end_of_working_in_department_date=end_of_working_in_department_date, position=position, department=department)

        try:
            db.session.add(employee)
            db.session.commit()
            return redirect('/employee')
        except:
            return "При добавлении сотрудника произошла ошибка"
    else:
        return render_template("create_employee.html")


@app.route('/employee/<int:id>/delete')
def employee_delete(id):
    employee = Employee.query.get_or_404(id)

    try:
        db.session.delete(employee)
        db.session.commit()
        return redirect('/employee')
    except:
        return "При удалении сотрудника произошла ошибка"


@app.route('/employee/<int:id>')
def employee_detail(id):
    employee = Employee.query.get(id)
    return render_template("employee_detail.html", employee=employee)


@app.route('/position')
def position():
    position = Position.query.order_by(Position.id.desc()).all()
    return render_template("position.html", position=position)


@app.route('/position/<int:id>/delete')
def position_delete(id):
    position = Position.query.get_or_404(id)

    try:
        db.session.delete(position)
        db.session.commit()
        return redirect('/position')
    except:
        return "При удалении должности произошла ошибка"


@app.route('/position/<int:id>/update', methods=['POST', 'GET'])
def position_update(id):
    position = Position.query.get(id)
    if request.method == "POST":
        position.title_of_position = request.form['title_of_position']
        position.short_title = request.form['short_title']
        position.cipher = request.form['cipher']
        position.low_border = request.form['low_border']
        position.high_border = request.form['high_border']

        try:
            db.session.commit()
            return redirect('/position')
        except:
            return "При радактировании должности произошла ошибка"
    else:
        return render_template("update_position.html", position=position)


@app.route('/create_position', methods=['POST', 'GET'])
def position_create():
    if request.method == "POST":
        title_of_position = request.form['title_of_position']
        short_title = request.form['short_title']
        cipher = request.form['cipher']
        low_border = request.form['low_border']
        high_border = request.form['high_border']

        position = Position(title_of_position=title_of_position, short_title=short_title,
        cipher=cipher, low_border=low_border, high_border=high_border)

        try:
            db.session.add(position)
            db.session.commit()
            return redirect('/position')
        except:
            return "При добавлении должности произошла ошибка"
    else:
        return render_template("create_position.html")


@app.route('/position/<int:id>')
def position_detail(id):
    position = Position.query.get(id)
    return render_template("position_detail.html", position=position)


@app.route('/department')
def department():
    department = Department.query.order_by(Department.id.desc()).all()
    return render_template("department.html", department=department)


@app.route('/department/<int:id>')
def department_detail(id):
    department = Department.query.get(id)
    return render_template("department_detail.html", department=department)


@app.route('/department/<int:id>/delete')
def department_delete(id):
    department = Department.query.get_or_404(id)

    try:
        db.session.delete(department)
        db.session.commit()
        return redirect('/department')
    except:
        return "При удалении подразделения произошла ошибка"


@app.route('/department/<int:id>/update', methods=['POST', 'GET'])
def department_update(id):
    department = Department.query.get(id)
    if request.method == "POST":
        department.name_of_department = request.form['name_of_department']
        department.head_of_department = request.form['head_of_department']

        try:
            db.session.commit()
            return redirect('/department')
        except:
            return "При радактировании подразделения произошла ошибка"
    else:
        return render_template("update_department.html", department=department)


@app.route('/create_department', methods=['GET', 'POST'])
def department_create():
    if request.method == "POST":
        name_of_department = request.form['name_of_department']
        head_of_department = request.form ['head_of_department']


        department = Department(name_of_department=name_of_department, head_of_department=head_of_department)

        try:
            db.session.add(department)
            db.session.commit()
            return redirect('/department')
        except:
            return "При добавлении подразделения произошла ошибка"
    else:
        return render_template("create_department.html")


@app.route('/company')
def company():
    company = Company.query.order_by(Company.id.desc()).all()
    return render_template("company.html", company=company)


@app.route('/company/<int:id>')
def company_detail(id):
    company = Company.query.get(id)
    return render_template("company_detail.html", company=company)


@app.route('/company/<int:id>/delete')
def company_delete(id):
    company = Company.query.get_or_404(id)

    try:
        db.session.delete(company)
        db.session.commit()
        return redirect('/company')
    except:
        return "При удалении предприятия произошла ошибка"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/company/<int:id>/update', methods=['POST', 'GET'])
def company_update(id):
    company = Company.query.get(id)
    if request.method == "POST":
        company.name_of_company = request.form['name_of_company']
        company.adress_of_company = request.form['adress_of_company']
        company.head_of_company = request.form['head_of_company']


        try:
            db.session.commit()
            return redirect('/company')
        except:
            return "При радактировании предприятия произошла ошибка"
    else:
        return render_template("update_company.html", company=company)


@app.route('/create_company', methods=['GET', 'POST'])
def company_create():
    if request.method == "POST":
        name_of_company = request.form['name_of_company']
        adress_of_company = request.form['adress_of_company']
        head_of_company = request.form['head_of_company']

        company = Company(name_of_company=name_of_company, adress_of_company=adress_of_company,
         head_of_company=head_of_company)

        try:
            db.session.add(company)
            db.session.commit()
            return redirect('/company')
        except:
            return "При добавлении предприятия произошла ошибка"
    else:
        return render_template("create_company.html")

@app.route('/relocation')
def relocation():
    relocation = Relocation.query.order_by(Relocation.id.desc()).all()
    return render_template("relocation.html", relocation=relocation)


@app.route('/relocation/<int:id>/update', methods=['POST', 'GET'])
def relocation_update(id):
    relocation = Relocation.query.get(id)
    if request.method == "POST":
        relocation.start_of_working_date = request.form['start_of_working_date']
        relocation.end_of_working_date = request.form['end_of_working_date']
        relocation.title_of_position = request.form['title_of_position']

        try:
            db.session.commit()
            return redirect('/relocation')
        except:
            return "При радактировании перемещения сотрудников произошла ошибка"
    else:
        return render_template("update_relocation.html", relocation=relocation)


@app.route('/create_relocation', methods=['GET', 'POST'])
def relocation_create():
    if request.method == "POST":
        start_of_working_date = request.form['start_of_working_date']
        end_of_working_date = request.form['end_of_working_date']
        title_of_position = request.form['title_of_position']

        relocation = Relocation(start_of_working_date=start_of_working_date, end_of_working_date=end_of_working_date,
                                title_of_position=title_of_position)

        try:
            db.session.add(relocation)
            db.session.commit()
            return redirect('/relocation')
        except:
            return "При добавлении перемещения сотрудников произошла ошибка"
    else:
        return render_template("create_relocation.html")


@app.route('/relocation/<int:id>/delete')
def relocation_delete(id):
    relocation = Relocation.query.get_or_404(id)

    try:
        db.session.delete(relocation)
        db.session.commit()
        return redirect('/relocation')
    except:
        return "При удалении перемещения сотрудников произошла ошибка"


@app.route('/relocate/<int:id>')
def relocation_detail(id):
    relocation = Relocation.query.get(id)
    return render_template("relocation_detail.html", relocation=relocation)


if __name__ == "__main__":
    app.run(debug=True)