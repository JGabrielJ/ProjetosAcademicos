package com.acxdev.prototypegaming.ui.fragment

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.acxdev.commonFunction.util.view.OtherViewX.Companion.html
import com.acxdev.prototypegaming.R
import com.acxdev.prototypegaming.databinding.FragmentOnBoarding2Binding

class FragmentOnBoarding2 : Fragment() {

    private lateinit var binding: FragmentOnBoarding2Binding
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        binding = FragmentOnBoarding2Binding.inflate(layoutInflater)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val string = "<font color=#FFFFFF>Não se preocupe com</font> <font color=#C7641E>Segurança</font>"
        binding.title.html(string)
    }
}