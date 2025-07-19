# src/modules/competition_follow/services/notification_service.py

import discord
import logging

logger = logging.getLogger(__name__)

class NotificationService:
    """
    负责向用户发送新作品通知。
    """

    def __init__(self, bot: discord.Client):
        self.bot = bot

    async def send_new_submission_notification(
        self, 
        user_id: int, 
        new_submission_id: str, 
        competition_message: discord.Message,
        competition_name: str
    ):
 
        try:
            user = await self.bot.fetch_user(user_id)
            if not user:
                logger.warning(f"无法找到用户 ID: {user_id}，通知发送失败。")
                return

            message_link = competition_message.jump_url
            
            embed = discord.Embed(
                title="🏆 杯赛更新通知",
                description=f"您关注的杯赛 **{competition_name}** 有了新的投稿！",
                color=discord.Color.blue()
            )
            embed.add_field(name="新投稿 ID", value=f"`{new_submission_id}`", inline=True)
            embed.add_field(name="快速跳转", value=f"[点击查看]({message_link})", inline=True)

            await user.send(embed=embed)
            logger.info(f"成功向用户 {user_id} 发送了关于比赛 '{competition_name}' 的新作品 {new_submission_id} 的通知。")

        except discord.Forbidden:
            logger.warning(f"无法向用户 {user_id} 发送私信。他们可能关闭了私信权限。")
        except Exception as e:
            logger.error(f"向用户 {user_id} 发送通知时发生未知错误: {e}", exc_info=True)

