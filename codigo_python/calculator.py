
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calcular_aliquota():
    try:
        receita_bruta = float(entry_receita_bruta.get().replace(',', '.'))
        anexo = combo_anexo.get()
        aplica_fator_r = var_fator_r.get()
        fator_r = 0
        if aplica_fator_r:
            fator_r = float(entry_fator_r.get().replace(',', '.'))
        
        if aplica_fator_r and fator_r >= 0.28:
            anexo = 'Anexo V'
        
        aliquota_efetiva = calcular_aliquota_efetiva(receita_bruta, anexo)
        result.set(f'{aliquota_efetiva:.3f}%')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

def calcular_aliquota_efetiva(receita_bruta, anexo):
    if anexo == 'Anexo III':
        return calcular_aliquota_anexo_iii(receita_bruta)
    elif anexo == 'Anexo IV':
        return calcular_aliquota_anexo_iv(receita_bruta)
    elif anexo == 'Anexo V':
        return calcular_aliquota_anexo_v(receita_bruta)
    else:
        return 0

def calcular_aliquota_anexo_iii(receita_bruta):
    faixas = [
        (180000.00, 0.06, 0.0),
        (360000.00, 0.112, 9360.0),
        (720000.00, 0.135, 17640.0),
        (1800000.00, 0.16, 35640.0),
        (3600000.00, 0.21, 125640.0),
        (4800000.00, 0.33, 648000.0)
    ]
    for faixa in faixas:
        if receita_bruta <= faixa[0]:
            aliquota_nominal = faixa[1]
            parcela_deduzir = faixa[2]
            aliquota_efetiva = ((receita_bruta * aliquota_nominal) - parcela_deduzir) / receita_bruta * 100
            # Aplicar ISSQN
            issqn = 0.325
            aliquota_efetiva_issqn = aliquota_efetiva * issqn
            return aliquota_efetiva_issqn

def calcular_aliquota_anexo_iv(receita_bruta):
    faixas = [
        (360000.00, 0.13, 12376.00),
        (720000.00, 0.18, 37376.00),
        (1800000.00, 0.225, 85376.00),
        (3600000.00, 0.275, 445376.00),
        (4800000.00, 0.33, 1045376.00)
    ]
    for faixa in faixas:
        if receita_bruta <= faixa[0]:
            aliquota_nominal = faixa[1]
            parcela_deduzir = faixa[2]
            aliquota_efetiva = ((receita_bruta * aliquota_nominal) - parcela_deduzir) / receita_bruta * 100
            return aliquota_efetiva

def calcular_aliquota_anexo_v(receita_bruta):
    faixas = [
        (180000.00, 0.155, 0.0),
        (360000.00, 0.18, 4500.0),
        (720000.00, 0.195, 9900.0),
        (1800000.00, 0.205, 17100.0),
        (3600000.00, 0.23, 62100.0),
        (4800000.00, 0.305, 540000.0)
    ]
    for faixa in faixas:
        if receita_bruta <= faixa[0]:
            aliquota_nominal = faixa[1]
            parcela_deduzir = faixa[2]
            aliquota_efetiva = ((receita_bruta * aliquota_nominal) - parcela_deduzir) / receita_bruta * 100
            # Aplicar ISSQN
            issqn = 0.325
            aliquota_efetiva_issqn = aliquota_efetiva * issqn
            return aliquota_efetiva_issqn

def limpar_dados():
    entry_receita_bruta.delete(0, tk.END)
    combo_anexo.set('')
    var_fator_r.set(False)
    entry_fator_r.delete(0, tk.END)
    result.set('')

# Configuração da Interface
root = tk.Tk()
root.title("Calculadora de Alíquota do Simples Nacional")
root.geometry("600x400")
root.configure(bg='black')

frame = tk.Frame(root, bg='black')
frame.pack(pady=20, padx=20, fill='both', expand=True)

# Campo Receita Bruta RBT12
tk.Label(frame, text="Receita Bruta RBT12:", bg='black', fg='white', font=("Arial", 14)).grid(row=0, column=0, sticky=tk.W)
entry_receita_bruta = tk.Entry(frame, font=("Arial", 14))
entry_receita_bruta.grid(row=0, column=1, padx=10, pady=5)

# Seleção do Anexo
tk.Label(frame, text="Anexo:", bg='black', fg='white', font=("Arial", 14)).grid(row=1, column=0, sticky=tk.W)
combo_anexo = ttk.Combobox(frame, values=["Anexo III", "Anexo IV", "Anexo V"], font=("Arial", 14))
combo_anexo.grid(row=1, column=1, padx=10, pady=5)

# Checkbox e Campo Fator R
var_fator_r = tk.BooleanVar()
chk_fator_r = tk.Checkbutton(frame, text="Aplica Fator R?", variable=var_fator_r, bg='black', fg='white', activebackground='black', activeforeground='white', font=("Arial", 14))
chk_fator_r.grid(row=2, column=0, sticky=tk.W)
entry_fator_r = tk.Entry(frame, font=("Arial", 14))
entry_fator_r.grid(row=2, column=1, padx=10, pady=5)

# Botões
btn_calcular = tk.Button(frame, text="Aliq%", command=calcular_aliquota, bg='orange', fg='black', width=3, height=2, borderwidth=0, highlightthickness=0, font=("Arial", 14))
btn_calcular.grid(row=3, column=0, padx=10, pady=20)

btn_limpar = tk.Button(frame, text="CE", command=limpar_dados, bg='orange', fg='black', width=3, height=2, borderwidth=0, highlightthickness=0, font=("Arial", 14))
btn_limpar.grid(row=3, column=1, padx=10, pady=20)

# Ajuste dos botões para serem circulares
btn_calcular.config(font=("Arial", 18), relief="flat")
btn_limpar.config(font=("Arial", 18), relief="flat")

# Fazer os botões circulares
btn_calcular.config(borderwidth=0, highlightthickness=0)
btn_calcular.grid(padx=10, pady=20, ipadx=20, ipady=20)

btn_limpar.config(borderwidth=0, highlightthickness=0)
btn_limpar.grid(padx=10, pady=20, ipadx=20, ipady=20)

# Resultado
result = tk.StringVar()
result.set('')
lbl_result = tk.Label(frame, textvariable=result, font=("Arial", 24), bg='black', fg='white')
lbl_result.grid(row=4, columnspan=2, pady=20)

root.mainloop()
