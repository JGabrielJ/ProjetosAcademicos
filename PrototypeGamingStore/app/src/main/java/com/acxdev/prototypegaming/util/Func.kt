package com.acxdev.prototypegaming.util

import java.text.DecimalFormat
import java.text.DecimalFormatSymbols
import java.util.*

class Func {
    companion object{
        fun Any?.toIDR(): String{
            val format = DecimalFormat("###,###,###,###,##0.##", DecimalFormatSymbols.getInstance(Locale("pt", "BR")))
            return "R$${format.format(toString().toBigDecimal())}"
        }
    }
}