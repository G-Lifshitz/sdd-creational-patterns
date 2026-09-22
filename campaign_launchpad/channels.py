
from abc import ABC, abstractmethod
from uuid import uuid4
from .budget import GlobalBudget
from .campaign import Campaign
from campaign_launchpad import budget

from campaign_launchpad import campaign


class ChannelClient(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def create_campaign(self, campaign: Campaign) -> str:
        # TODO: Create a campaign on this channel and return an external id.
        pass

    @abstractmethod
    def pause_campaign(self, campaign_id: str) -> None:
        pass


class GoogleAdsClient(ChannelClient):
  def __init__(self, name):
     self.name = 'google'
  def create_campaign(self, campaign: Campaign):
     budget = GlobalBudget()
     budget.allocate(campaign.daily_budget)
     return f"g-{uuid4()}" #formatted string & google prefix
  def pause_campaign(self, campaign_id: str):
    pass

class FacebookAdsClient(ChannelClient):
  def __init__(self, name):
     self.name = 'facebook'

  def create_campaign(self, campaign):
     budget = GlobalBudget()
     budget.allocate(campaign.daily_budget)
     return f"f-{uuid4()}" 
  def pause_campaign(self, campaign_id):
    pass

class ChannelClientFactory:
    @staticmethod
    def create(channel: str) -> ChannelClient:
      if channel == 'google':
          return GoogleAdsClient(channel)
      elif channel == 'facebook':
          return FacebookAdsClient(channel)
      else: 
         raise ValueError("Unsupported channel: {channel}")
      pass  
