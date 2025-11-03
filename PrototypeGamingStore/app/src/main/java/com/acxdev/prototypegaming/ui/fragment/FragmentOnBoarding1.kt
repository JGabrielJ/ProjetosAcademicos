package com.acxdev.prototypegaming.ui.fragment

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.acxdev.commonFunction.util.view.OtherViewX.Companion.html
import com.acxdev.prototypegaming.R
import com.acxdev.prototypegaming.databinding.FragmentOnBoarding1Binding

class FragmentOnBoarding1 : Fragment() {

    private lateinit var binding: FragmentOnBoarding1Binding
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        binding = FragmentOnBoarding1Binding.inflate(layoutInflater)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val string = "<font color=#FFFFFF>Batalhe por cada uma das</font> <font color=#6E2CC9>Conquistas Disponíveis</font>"
        binding.title.html(string)
    }
}