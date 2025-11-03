package com.acxdev.prototypegaming.ui.activity

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.viewpager.widget.ViewPager
import com.acxdev.commonFunction.adapter.PageAdapter
import com.acxdev.commonFunction.util.FunctionX.Companion.putExtra
import com.acxdev.prototypegaming.ui.fragment.FragmentOnBoarding
import com.acxdev.prototypegaming.databinding.ActivityOnBoardingBinding
import com.acxdev.prototypegaming.ui.fragment.FragmentOnBoarding1
import com.acxdev.prototypegaming.ui.fragment.FragmentOnBoarding2

class ActivityOnBoarding : AppCompatActivity() {
    private lateinit var binding: ActivityOnBoardingBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityOnBoardingBinding.inflate(layoutInflater)
        setContentView(binding.root)
        val page = PageAdapter(supportFragmentManager)
        page.adds(FragmentOnBoarding(), FragmentOnBoarding1(), FragmentOnBoarding2())
        binding.viewPager.adapter = page
        binding.dotsIndicator.setViewPager(binding.viewPager)
        var current = 0
        binding.next.setOnClickListener {
            if(current < 2) {
                current += 1
                binding.viewPager.currentItem = current
            }
            else {
                finish()
                startActivity(Intent(this, ActivityMain::class.java))
            }
        }
        binding.viewPager.addOnPageChangeListener(object : ViewPager.OnPageChangeListener {
            override fun onPageScrolled(position: Int, positionOffset: Float, positionOffsetPixels: Int) {}

            override fun onPageSelected(position: Int) {
                when (position) {
                    0 -> current = 0
                    1 -> current = 1
                    2 ->  current = 2
                }
            }

            override fun onPageScrollStateChanged(state: Int) {}
        })
    }
}