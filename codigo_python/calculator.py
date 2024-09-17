import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calcular_aliquota():
    try:
        receita_bruta = float(entry_receita_bruta.get().replace(',', '.'))
        meses_atividade = int(entry_meses_atividade.get())
        if meses_atividade < 1 or meses_atividade > 12:
            messagebox.showerror("Erro", "Meses de atividade deve estar entre 1 e 12.")
            return

        aplica_fator_r = var_fator_r.get()
        fator_r = 0
        if aplica_fator_r:
            fator_r = float(entry_fator_r.get().replace(',', '.'))
            if fator_r >= 0.28:
                anexo = 'Anexo III'
            else:
                anexo = 'Anexo V'
        else:
            anexo = combo_anexo.get()

        # Verificar se o anexo foi selecionado
        if not anexo:
            messagebox.showerror("Erro", "Por favor, selecione um anexo.")
            return

        aliquota_efetiva, percentual_iss, aliquota_iss = calcular_aliquota_efetiva(receita_bruta, anexo, meses_atividade)
        result.set(f'Alíquota Efetiva Total: {aliquota_efetiva*100:.2f}%\n'
                   f'Percentual de Repartição do ISS: {percentual_iss*100:.2f}%\n'
                   f'Alíquota Efetiva do ISS: {aliquota_iss*100:.2f}%')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

def calcular_aliquota_efetiva(receita_bruta, anexo, meses_atividade):
    if anexo == 'Anexo III':
        return calcular_aliquota_anexo_iii(receita_bruta, meses_atividade)
    elif anexo == 'Anexo IV':
        return calcular_aliquota_anexo_iv(receita_bruta, meses_atividade)
    elif anexo == 'Anexo V':
        return calcular_aliquota_anexo_v(receita_bruta, meses_atividade)
    else:
        return 0, 0, 0

def ajustar_faixas(faixas, meses_atividade):
    fator = meses_atividade / 12.0
    faixas_ajustadas = []
    for faixa in faixas:
        faixa_final = faixa[0] * fator
        faixas_ajustadas.append((faixa_final,) + faixa[1:])
    return faixas_ajustadas

def calcular_aliquota_anexo_iii(receita_bruta, meses_atividade):
    faixas = [
        (180000.00, 0.06, 0.00, 0.3350),
        (360000.00, 0.112, 9360.00, 0.3200),
        (720000.00, 0.135, 17640.00, 0.3250),
        (1800000.00, 0.16, 35640.00, 0.3250),
        (3600000.00, 0.21, 125640.00, 0.3350),
        (4800000.00, 0.33, 648000.00, 0.00)
    ]
    faixas_ajustadas = ajustar_faixas(faixas, meses_atividade)
    for faixa in faixas_ajustadas:
        if receita_bruta <= faixa[0]:
            aliquota_nominal = faixa[1]
            parcela_deduzir = faixa[2]
            percentual_iss = faixa[3]
            aliquota_efetiva = (receita_bruta * aliquota_nominal - parcela_deduzir) / receita_bruta
            aliquota_iss = aliquota_efetiva * percentual_iss
            # Aplicar o limite máximo de 5% ao ISS
            if aliquota_iss > 0.05:
                aliquota_iss = 0.05
            return aliquota_efetiva, percentual_iss, aliquota_iss
    return 0, 0, 0

def calcular_aliquota_anexo_iv(receita_bruta, meses_atividade):
    faixas = [
        (180000.00, 0.045, 0.00, 0.0),  # No Anexo IV, o ISS é recolhido fora do Simples
        (360000.00, 0.09, 8100.00, 0.0),
        (720000.00, 0.102, 12420.00, 0.0),
        (1800000.00, 0.14, 39780.00, 0.0),
        (3600000.00, 0.22, 183780.00, 0.0),
        (4800000.00, 0.33, 828000.00, 0.0)
    ]
    faixas_ajustadas = ajustar_faixas(faixas, meses_atividade)
    for faixa in faixas_ajustadas:
        if receita_bruta <= faixa[0]:
            aliquota_nominal = faixa[1]
            parcela_deduzir = faixa[2]
            percentual_iss = faixa[3]  # Será 0 no Anexo IV
            aliquota_efetiva = (receita_bruta * aliquota_nominal - parcela_deduzir) / receita_bruta
            aliquota_iss = 0  # ISS recolhido fora do Simples no Anexo IV
            return aliquota_efetiva, percentual_iss, aliquota_iss
    return 0, 0, 0

def calcular_aliquota_anexo_v(receita_bruta, meses_atividade):
    faixas = [
        (180000.00, 0.155, 0.00, 0.28),
        (360000.00, 0.18, 4500.00, 0.335),
        (720000.00, 0.195, 9900.00, 0.35),
        (1800000.00, 0.205, 17100.00, 0.355),
        (3600000.00, 0.23, 62100.00, 0.365),
        (4800000.00, 0.305, 540000.00, 0.00)
    ]
    faixas_ajustadas = ajustar_faixas(faixas, meses_atividade)
    for faixa in faixas_ajustadas:
        if receita_bruta <= faixa[0]:
            aliquota_nominal = faixa[1]
            parcela_deduzir = faixa[2]
            percentual_iss = faixa[3]
            aliquota_efetiva = (receita_bruta * aliquota_nominal - parcela_deduzir) / receita_bruta
            aliquota_iss = aliquota_efetiva * percentual_iss
            # Aplicar o limite máximo de 5% ao ISS
            if aliquota_iss > 0.05:
                aliquota_iss = 0.05
            return aliquota_efetiva, percentual_iss, aliquota_iss
    return 0, 0, 0

def limpar_dados():
    entry_receita_bruta.delete(0, tk.END)
    combo_anexo.set('')
    var_fator_r.set(False)
    entry_fator_r.delete(0, tk.END)
    entry_meses_atividade.delete(0, tk.END)
    result.set('')

# Configuração da Interface
root = tk.Tk()
root.title("Calculadora de Alíquota do Simples Nacional")
root.geometry("600x500")
root.configure(bg='black')

frame = tk.Frame(root, bg='black')
frame.pack(pady=20, padx=20, fill='both', expand=True)

# Campo Receita Bruta RBT12
tk.Label(frame, text="Receita Bruta RBT12:", bg='black', fg='white', font=("Arial", 14)).grid(row=0, column=0, sticky=tk.W)
entry_receita_bruta = tk.Entry(frame, font=("Arial", 14))
entry_receita_bruta.grid(row=0, column=1, padx=10, pady=5)

# Campo Meses de Atividade
tk.Label(frame, text="Meses de Atividade:", bg='black', fg='white', font=("Arial", 14)).grid(row=1, column=0, sticky=tk.W)
entry_meses_atividade = tk.Entry(frame, font=("Arial", 14))
entry_meses_atividade.grid(row=1, column=1, padx=10, pady=5)
entry_meses_atividade.insert(0, "12")  # Valor padrão

# Seleção do Anexo
tk.Label(frame, text="Anexo:", bg='black', fg='white', font=("Arial", 14)).grid(row=2, column=0, sticky=tk.W)
combo_anexo = ttk.Combobox(frame, values=["Anexo III", "Anexo IV", "Anexo V"], font=("Arial", 14))
combo_anexo.grid(row=2, column=1, padx=10, pady=5)

# Checkbox e Campo Fator R
var_fator_r = tk.BooleanVar()
chk_fator_r = tk.Checkbutton(frame, text="Aplica Fator R?", variable=var_fator_r, bg='black', fg='white', activebackground='black', activeforeground='white', font=("Arial", 14))
chk_fator_r.grid(row=3, column=0, sticky=tk.W)
entry_fator_r = tk.Entry(frame, font=("Arial", 14))
entry_fator_r.grid(row=3, column=1, padx=10, pady=5)

# Botões
btn_calcular = tk.Button(frame, text="Calcular", command=calcular_aliquota, bg='orange', fg='black', width=10, height=2, font=("Arial", 14))
btn_calcular.grid(row=4, column=0, padx=10, pady=20)

btn_limpar = tk.Button(frame, text="Limpar", command=limpar_dados, bg='orange', fg='black', width=10, height=2, font=("Arial", 14))
btn_limpar.grid(row=4, column=1, padx=10, pady=20)

# Resultado
result = tk.StringVar()
result.set('')
lbl_result = tk.Label(frame, textvariable=result, font=("Arial", 14), bg='black', fg='white')
lbl_result.grid(row=5, columnspan=2, pady=20)

root.mainloop()
