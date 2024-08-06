Option Explicit

' Calcular a alíquota efetiva
Sub CalcularAliquota()
    Dim receitaBruta As Double
    Dim anexo As String
    Dim aplicaFatorR As Boolean
    Dim aliquotaEfetiva As Double
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Sheet1") ' Nome da planilha onde os dados estão

    Dim i As Long
    For i = 2 To ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
        receitaBruta = ws.Cells(i, 1).Value ' Supondo que a Receita Bruta está na coluna A
        anexo = ws.Cells(i, 2).Value ' Supondo que o Anexo está na coluna B
        aplicaFatorR = ws.Cells(i, 3).Value ' Supondo que o Fator R está na coluna C

        If aplicaFatorR Then
            anexo = "Anexo V"
        End If

        aliquotaEfetiva = CalcularAliquotaEfetiva(receitaBruta, anexo)
        ws.Cells(i, 5).Value = Format(aliquotaEfetiva, "#.##") & "%" ' Colocando a alíquota na coluna E
    Next i
End Sub

' Determina qual anexo usar para o cálculo
Function CalcularAliquotaEfetiva(receitaBruta As Double, anexo As String) As Double
    Select Case anexo
        Case "Anexo III"
            CalcularAliquotaEfetiva = CalcularAliquotaAnexoIII(receitaBruta)
        Case "Anexo IV"
            CalcularAliquotaEfetiva = CalcularAliquotaAnexoIV(receitaBruta)
        Case "Anexo V"
            CalcularAliquotaEfetiva = CalcularAliquotaAnexoV(receitaBruta)
        Case Else
            CalcularAliquotaEfetiva = 0
    End Select
End Function

' Cálculo da alíquota para o Anexo III
Function CalcularAliquotaAnexoIII(receitaBruta As Double) As Double
    Dim faixas As Variant
    faixas = Array(Array(180000, 0.06, 0), Array(360000, 0.112, 9360), _
                   Array(720000, 0.135, 17640), Array(1800000, 0.16, 35640), _
                   Array(3600000, 0.21, 125640), Array(4800000, 0.33, 648000))

    Dim i As Integer
    For i = LBound(faixas) To UBound(faixas)
        If receitaBruta <= faixas(i)(0) Then
            Dim aliquotaNominal As Double
            Dim parcelaDeduzir As Double
            Dim aliquotaEfetiva As Double
            aliquotaNominal = faixas(i)(1)
            parcelaDeduzir = faixas(i)(2)
            aliquotaEfetiva = ((receitaBruta * aliquotaNominal) - parcelaDeduzir) / receitaBruta * 100
            ' Aplicar ISSQN
            CalcularAliquotaAnexoIII = aliquotaEfetiva * 0.325
            Exit Function
        End If
    Next i
End Function

' Cálculo da alíquota para o Anexo IV
Function CalcularAliquotaAnexoIV(receitaBruta As Double) As Double
    Dim faixas As Variant
    faixas = Array(Array(360000, 0.13, 12376), Array(720000, 0.18, 37376), _
                   Array(1800000, 0.225, 85376), Array(3600000, 0.275, 445376), _
                   Array(4800000, 0.33, 1045376))

    Dim i As Integer
    For i = LBound(faixas) To UBound(faixas)
        If receitaBruta <= faixas(i)(0) Then
            Dim aliquotaNominal As Double
            Dim parcelaDeduzir As Double
            Dim aliquotaEfetiva As Double
            aliquotaNominal = faixas(i)(1)
            parcelaDeduzir = faixas(i)(2)
            aliquotaEfetiva = ((receitaBruta * aliquotaNominal) - parcelaDeduzir) / receitaBruta * 100
            CalcularAliquotaAnexoIV = aliquotaEfetiva
            Exit Function
        End If
    Next i
End Function

' Cálculo da alíquota para o Anexo V
Function CalcularAliquotaAnexoV(receitaBruta As Double) As Double
    Dim faixas As Variant
    faixas = Array(Array(180000, 0.155, 0), Array(360000, 0.18, 4500), _
                   Array(720000, 0.195, 9900), Array(1800000, 0.205, 17100), _
                   Array(3600000, 0.23, 62100), Array(4800000, 0.305, 540000))

    Dim i As Integer
    For i = LBound(faixas) To UBound(faixas)
        If receitaBruta <= faixas(i)(0) Then
            Dim aliquotaNominal As Double
            Dim parcelaDeduzir As Double
            Dim aliquotaEfetiva As Double
            aliquotaNominal = faixas(i)(1)
            parcelaDeduzir = faixas(i)(2)
            aliquotaEfetiva = ((receitaBruta * aliquotaNominal) - parcelaDeduzir) / receitaBruta * 100
            ' Aplicar ISSQN
            CalcularAliquotaAnexoV = aliquotaEfetiva * 0.325
            Exit Function
        End If
    Next i
End Function
