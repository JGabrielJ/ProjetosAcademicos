package com.acxdev.prototypegaming.adapter

import android.content.Intent
import com.acxdev.commonFunction.adapter.BaseAdapter
import com.acxdev.prototypegaming.common.Constant
import com.acxdev.prototypegaming.databinding.ItemMessageBinding
import com.acxdev.prototypegaming.model.Friendships
import com.acxdev.prototypegaming.ui.activity.ActivityChat
import com.acxdev.prototypegaming.ui.activity.ActivityDetail
import com.google.gson.Gson

class ItemMessage(private val list: MutableList<Friendships>): BaseAdapter<ItemMessageBinding>(ItemMessageBinding::inflate, list) {
    override fun onBindViewHolder(holder: ViewHolder<ItemMessageBinding>, position: Int) {
        val list = list[position]
        holder.binding.sendDate.text = context.getString(list.sendDate)
        holder.binding.lastMessage.text = context.getString(list.lastMessage)
        holder.binding.name.text = context.getString(list.name)
        holder.binding.image.setImageResource(list.image)
        holder.itemView.setOnClickListener {
            context.startActivity(
                Intent(context, ActivityChat::class.java).putExtra(Constant.DATA, Gson().toJson(list))
            )
        }
    }
}