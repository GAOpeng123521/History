/******************** (C) COPYRIGHT  ***************************
 * 文件名  ：uart.C
 * 描述    ：   
 * 库版本  ： 
 * 作者    ：
 * 博客    ：
 *修改时间 ：

*****************************************************************/
#include "uart.h"

void UART_Config(void)
{
  UART1->CR1 = (0<<4)|(0<<3)|(0<<2)|(0<<1)|(0<<0);//1位起始位8位数据位，CR3决定停止位，不使用奇偶校验位，不使能奇偶校验功能
  UART1->CR2 = (0<<7)|(0<<6)|(1<<5)|(0<<4)|(1<<3)|(1<<2);//使能发送、接收 接收中断使能 禁止发送中断
  UART1->CR3 = (0<<6)|(0<<5)|(0<<4)|(0<<3); //设置1位停止位 不使能SCLK
  
  //设置波特率    
  //16M/9600=1667=683H
  UART1->BRR2 = 0x03; 
  UART1->BRR1 = 0x68;
  
  
  UART1->CR1 &= ~(1<<5);//使能uart
}


/*************发送一个字节函数*****************/
void UART1_SendByte(unsigned char data)
{
    while (!(UART1->SR & 0x80)); //数据转移完成
    UART1->DR=data;
    while(!(UART1->SR & 0x40));  //发送完成
}


