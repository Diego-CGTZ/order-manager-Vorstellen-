from flask import Blueprint, render_template, redirect, url_for, request, flash
import sirope
from app.forms.cliente_form import ClienteForm
from app.models.cliente import Cliente

cliente_bp = Blueprint("cliente", __name__, url_prefix="/clientes")

@cliente_bp.route("/")
def listar_clientes():
    srp = sirope.Sirope()
    clientes = list(srp.find(Cliente))
    return render_template("clientes/listar.html", clientes=clientes)

@cliente_bp.route("/nuevo", methods=["GET", "POST"])
def nuevo_cliente():
    srp = sirope.Sirope()
    form = ClienteForm()

    if form.validate_on_submit():
        cliente = Cliente(form.nombre.data, form.email.data, form.telefono.data)
        srp.save(cliente)
        flash("Cliente creado correctamente.", "success")
        return redirect(url_for("cliente.listar_clientes"))

    return render_template("clientes/form.html", form=form, titulo="Nuevo Cliente")

@cliente_bp.route("/editar/<nombre>", methods=["GET", "POST"])
def editar_cliente(nombre):
    srp = sirope.Sirope()
    cliente = next(srp.find(Cliente, lambda c: c.nombre == nombre), None)

    if not cliente:
        flash("Cliente no encontrado.", "error")
        return redirect(url_for("cliente.listar_clientes"))

    form = ClienteForm(obj=cliente)

    if form.validate_on_submit():
        cliente.nombre = form.nombre.data
        cliente.email = form.email.data
        cliente.telefono = form.telefono.data
        srp.save(cliente)
        flash("Cliente actualizado correctamente.", "success")
        return redirect(url_for("cliente.listar_clientes"))

    return render_template("clientes/form.html", form=form, titulo="Editar Cliente")

@cliente_bp.route("/eliminar/<nombre>", methods=["POST"])
def eliminar_cliente(nombre):
    srp = sirope.Sirope()
    cliente = next(srp.find(Cliente, lambda c: c.nombre == nombre), None)

    if cliente:
        srp.delete(cliente)
        flash("Cliente eliminado correctamente.", "success")
    else:
        flash("Cliente no encontrado.", "error")

    return redirect(url_for("cliente.listar_clientes"))
