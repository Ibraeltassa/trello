from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.forms import TaskForm
from app.models import Task, db

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/dashboard")
@login_required
def dashboard_view():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html", tasks=tasks)

@dashboard.route("/task/new", methods=["GET", "POST"])
@login_required
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, description=form.description.data, status=form.status.data, owner=current_user)
        db.session.add(task)
        db.session.commit()
        flash("Tarefa criada!", "success")
        return redirect(url_for("dashboard.dashboard_view"))
    return render_template("tasks.html", form=form)

@dashboard.route("/task/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_task(id):
    task = Task.query.get_or_404(id)
    if task.owner != current_user:
        flash("Acesso negado!", "danger")
        return redirect(url_for("dashboard.dashboard_view"))
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.status = form.status.data
        db.session.commit()
        flash("Tarefa atualizada!", "success")
        return redirect(url_for("dashboard.dashboard_view"))
    return render_template("tasks.html", form=form)

@dashboard.route("/task/<int:id>/delete")
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)
    if task.owner != current_user:
        flash("Acesso negado!", "danger")
        return redirect(url_for("dashboard.dashboard_view"))
    db.session.delete(task)
    db.session.commit()
    flash("Tarefa excluída!", "success")
    return redirect(url_for("dashboard.dashboard_view"))
