package com.acxdev.prototypegaming.ui.activity

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.recyclerview.widget.RecyclerView
import com.acxdev.commonFunction.util.view.RecyclerViewX.Companion.adapter
import com.acxdev.prototypegaming.R
import com.acxdev.prototypegaming.adapter.RowMessage
import com.acxdev.prototypegaming.common.Constant
import com.acxdev.prototypegaming.databinding.ActivityChatBinding
import com.acxdev.prototypegaming.model.ChatMessage

class ActivityChat : AppCompatActivity() {
    private lateinit var binding: ActivityChatBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_chat)
        binding.messagesSent.adapter(RowMessage(Constant.rowMessage()), 1)
    }
}