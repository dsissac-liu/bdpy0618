from decimal import Decimal as Dec

print Dec(2.968)
print Dec('2.968')
print Dec(0.001)*Dec(2968)-Dec(2.968)
print Dec('0.001')*Dec(2968)-Dec('2.968')
print Dec(0.0001)
print Dec(0.0001)*Dec(296.8)-Dec(2.968)
print Dec('0.002')*Dec(2968)-Dec('2.968')
