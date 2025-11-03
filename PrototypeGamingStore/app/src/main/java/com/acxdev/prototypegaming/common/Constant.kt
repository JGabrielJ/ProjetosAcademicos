package com.acxdev.prototypegaming.common

import com.acxdev.prototypegaming.R
import com.acxdev.prototypegaming.adapter.ItemMessage
import com.acxdev.prototypegaming.adapter.RowMessage
import com.acxdev.prototypegaming.model.*

class Constant {
    companion object{

        const val DATA = "data"

        fun headerGame(): MutableList<Game>{
            val imageListDota = mutableListOf<Int>()
            imageListDota.add(R.drawable.ic_dota_1)
            imageListDota.add(R.drawable.ic_dota_2)
            imageListDota.add(R.drawable.ic_dota_3)
            imageListDota.add(R.drawable.ic_dota_4)

            val imageListValorant = mutableListOf<Int>()
            imageListValorant.add(R.drawable.ic_valorant_1)
            imageListValorant.add(R.drawable.ic_valorant_2)
            imageListValorant.add(R.drawable.ic_valorant_3)
            imageListValorant.add(R.drawable.ic_valorant_4)

            val header = mutableListOf<Game>()
            header.add(Game(R.string.valorant, R.string.tacticalshooter, R.drawable.ic_valorant_logo, R.string.descValorant, R.drawable.ic_valorant,null, imageListValorant))
            header.add(Game(R.string.dota2, R.string.moba, R.drawable.ic_dota_logo, R.string.descDota, R.drawable.ic_dota,null, imageListDota))
            return header
        }

        fun popularGames(): MutableList<Game>{
            val imageListGenshin = mutableListOf<Int>()
            imageListGenshin.add(R.drawable.ic_genshin_1)
            imageListGenshin.add(R.drawable.ic_genshin_2)
            imageListGenshin.add(R.drawable.ic_genshin_3)
            imageListGenshin.add(R.drawable.ic_genshin_4)

            val imageListRe = mutableListOf<Int>()
            imageListRe.add(R.drawable.ic_re_1)
            imageListRe.add(R.drawable.ic_re_2)

            val imageListGta = mutableListOf<Int>()
            imageListGta.add(R.drawable.ic_gta_1)
            imageListGta.add(R.drawable.ic_gta_2)
            imageListGta.add(R.drawable.ic_gta_3)
            imageListGta.add(R.drawable.ic_gta_4)

            val popular = mutableListOf<Game>()
            popular.add(Game(R.string.genshinImpact, R.string.rpg, null, R.string.descGenshin, R.drawable.ic_genshin,null, imageListGenshin))
            popular.add(Game(R.string.revillage, R.string.survivalHorror, null, R.string.descRe, R.drawable.ic_re,179.99, imageListRe))
            popular.add(Game(R.string.gtav, R.string.actionAdventure, null, R.string.descGta, R.drawable.ic_gta,89.99, imageListGta))
            return popular
        }

        fun freeToPlayGame(): MutableList<Game>{
            val imageListApex = mutableListOf<Int>()
            imageListApex.add(R.drawable.ic_apex_1)
            imageListApex.add(R.drawable.ic_apex_2)
            imageListApex.add(R.drawable.ic_apex_3)

            val freeToPlay = mutableListOf<Game>()
            freeToPlay.add(Game(R.string.apex, R.string.battleRoyale, null, R.string.descApex, R.drawable.ic_apex,null, imageListApex))
            return freeToPlay
        }

        fun spec(): MutableList<Spec>{
            val spec = mutableListOf<Spec>()
            spec.add(Spec("Minimum Specs","30fps","Intel i3-370M","RAM 4GB","Intel HD 4000"))
            spec.add(Spec("Rec, Specs","60fps","Core i5-4150","RAM 4GB","GeForce GT 730"))
            spec.add(Spec("Ultra Specs","144fps+","Core i5-4460","RAM 8GB","NVIDIA GTX 1050 Ti"))
            return spec
        }

        fun itemMessage(): MutableList<Friendships> {
            val itemMsg = mutableListOf<Friendships>()
            itemMsg.add(Friendships(R.drawable.ic_mario, R.string.nameJG, R.string.lastJG,R.string.dateJG, 0))
            itemMsg.add(Friendships(R.drawable.ic_usopp, R.string.nameHades, R.string.lastHades,R.string.dateHades, 1))
            itemMsg.add(Friendships(R.drawable.ic_sigma, R.string.nameHumano, R.string.lastHumano,R.string.dateHumano, 2))
            itemMsg.add(Friendships(R.drawable.ic_amogus, R.string.nameHumana, R.string.lastHumana,R.string.dateHumana, 3))
            return itemMsg
        }

        fun rowMessage(profile: Profile): MutableList<ChatMessage> {
            val msg = mutableListOf<ChatMessage>()
            when (profile) {
                Profile.PROFILE_JG -> {
                    msg.add(ChatMessage(R.drawable.ic_mario, R.string.nameJG, R.string.firstMsg, R.string.firstDate))
                    msg.add(ChatMessage(R.drawable.ic_mario, R.string.nameJG, R.string.genericMsg, R.string.genericDate))
                    msg.add(ChatMessage(R.drawable.ic_mario, R.string.nameJG, R.string.lastJG, R.string.dateJG))
                }
                Profile.PROFILE_HADES -> {
                    msg.add(ChatMessage(R.drawable.ic_usopp, R.string.nameHades, R.string.firstMsg, R.string.firstDate))
                    msg.add(ChatMessage(R.drawable.ic_usopp, R.string.nameHades, R.string.genericMsg, R.string.genericDate))
                    msg.add(ChatMessage(R.drawable.ic_usopp, R.string.nameHades, R.string.lastHades,R.string.dateHades))
                }
                Profile.PROFILE_SIGMA -> {
                    msg.add(ChatMessage(R.drawable.ic_sigma, R.string.nameHumano, R.string.firstMsg, R.string.firstDate))
                    msg.add(ChatMessage(R.drawable.ic_sigma, R.string.nameHumano, R.string.genericMsg, R.string.genericDate))
                    msg.add(ChatMessage(R.drawable.ic_sigma, R.string.nameHumano, R.string.lastHumano,R.string.dateHumano))
                }
                Profile.PROFILE_DUVIDOSA -> {
                    msg.add(ChatMessage(R.drawable.ic_amogus, R.string.nameHumana, R.string.firstMsg, R.string.firstDate))
                    msg.add(ChatMessage(R.drawable.ic_amogus, R.string.nameHumana, R.string.genericMsg, R.string.genericDate))
                    msg.add(ChatMessage(R.drawable.ic_amogus, R.string.nameHumana, R.string.lastHumana,R.string.dateHumana))
                }
                else -> {}
            }
            return msg
        }
    }
}