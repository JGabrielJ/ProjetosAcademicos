package com.acxdev.prototypegaming.ui.fragment

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.acxdev.commonFunction.util.view.RecyclerViewX.Companion.adapter
import com.acxdev.prototypegaming.R
import com.acxdev.prototypegaming.adapter.ItemMessage
import com.acxdev.prototypegaming.adapter.RowHeader
import com.acxdev.prototypegaming.common.Constant
import com.acxdev.prototypegaming.databinding.FragmentChatBinding

class FragmentChat : Fragment() {

    private lateinit var binding: FragmentChatBinding
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        binding = FragmentChatBinding.inflate(layoutInflater)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        binding.messages.adapter(ItemMessage(Constant.itemMessage()), 1)
    }
}