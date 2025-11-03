package com.acxdev.prototypegaming.adapter

import android.content.Intent
import com.acxdev.commonFunction.adapter.BaseAdapter
import com.acxdev.prototypegaming.common.Constant
import com.acxdev.prototypegaming.databinding.ItemMessageBinding
import com.acxdev.prototypegaming.databinding.RowMessageBinding
import com.acxdev.prototypegaming.model.ChatMessage
import com.acxdev.prototypegaming.model.Friendships
import com.acxdev.prototypegaming.ui.activity.ActivityChat
import com.google.gson.Gson

class RowMessage(private val list: MutableList<ChatMessage>): BaseAdapter<RowMessageBinding>(RowMessageBinding::inflate, list) {
    override fun onBindViewHolder(holder: ViewHolder<RowMessageBinding>, position: Int) {
        val list = list[position]
        holder.binding.img.setImageResource(list.img)
        holder.binding.friend.text = context.getString(list.friend)
        holder.binding.content.text = context.getString(list.content)
        holder.binding.date.text = context.getString(list.date)
    }
}