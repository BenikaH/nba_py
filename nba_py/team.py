from nba_py import _api_scrape, _get_json
from nba_py import constants


class TeamList:
    _endpoint = 'commonteamyears'

    def __init__(self,
                 league_id=constants.League.NBA):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id})

    def info(self):
        return _api_scrape(self.json, 0)


class TeamSummary:
    _endpoint = 'teaminfocommon'

    def __init__(self,
                 team_id,
                 season=constants.CURRENT_SEASON,
                 league_id=constants.League.NBA,
                 season_type=constants.SeasonType.Default):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'TeamID': team_id,
                                      'Season': season,
                                      'LeagueID': league_id,
                                      'SeasonType': season_type})

    def info(self):
        return _api_scrape(self.json, 0)

    def season_ranks(self):
        return _api_scrape(self.json, 1)


class TeamDetails:
    _endpoint = 'teamdetails'

    def __init__(self, team_id):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'TeamID': team_id})

    def background(self):
        return _api_scrape(self.json, 0)

    def history(self):
        return _api_scrape(self.json, 1)

    def social_sites(self):
        return _api_scrape(self.json, 2)

    def awards_championships(self):
        return _api_scrape(self.json, 3)

    def awards_conf(self):
        return _api_scrape(self.json, 4)

    def awards_div(self):
        return _api_scrape(self.json, 5)

    def hof(self):
        return _api_scrape(self.json, 6)

    def retired(self):
        return _api_scrape(self.json, 7)


class TeamCommonRoster:
    _endpoint = 'commonteamroster'

    def __init__(self,
                 team_id,
                 season=constants.CURRENT_SEASON):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'TeamID': team_id,
                                      'Season': season})

    def roster(self):
        return _api_scrape(self.json, 0)

    def coaches(self):
        return _api_scrape(self.json, 1)


class _TeamDashboard:
    _endpoint = ''

    def __init__(self,
                 team_id,
                 measure_type=constants.MeasureType.Default,
                 per_mode=constants.PerMode.Default,
                 plus_minus=constants.PlusMinus.Default,
                 pace_adjust=constants.PaceAdjust.Default,
                 rank=constants.Rank.Default,
                 league_id=constants.League.Default,
                 season=constants.CURRENT_SEASON,
                 season_type=constants.SeasonType.Default,
                 po_round=constants.PlayoffRound.Default,
                 outcome=constants.Outcome.Default,
                 location=constants.Location.Default,
                 month=constants.Month.Default,
                 season_segment=constants.SeasonSegment.Default,
                 date_from=constants.DateFrom.Default,
                 date_to=constants.DateTo.Default,
                 opponent_team_id=constants.OpponentTeamID.Default,
                 vs_conference=constants.VsConference.Default,
                 vs_division=constants.VsDivision.Default,
                 game_segment=constants.GameSegment.Default,
                 period=constants.Period.Default,
                 shot_clock_range=constants.ShotClockRange.Default,
                 last_n_games=constants.LastNGames.Default):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'TeamID': team_id,
                                      'MeasureType': measure_type,
                                      'PerMode': per_mode,
                                      'PlusMinus': plus_minus,
                                      'PaceAdjust': pace_adjust,
                                      'Rank': rank,
                                      'LeagueID': league_id,
                                      'Season': season,
                                      'SeasonType': season_type,
                                      'PORound': po_round,
                                      'Outcome': outcome,
                                      'Location': location,
                                      'Month': month,
                                      'SeasonSegment': season_segment,
                                      'DateFrom': date_from,
                                      'DateTo': date_to,
                                      'OpponentTeamID': opponent_team_id,
                                      'VsConference': vs_conference,
                                      'VsDivision': vs_division,
                                      'GameSegment': game_segment,
                                      'Period': period,
                                      'ShotClockRange': shot_clock_range,
                                      'LastNGames': last_n_games})

    def overall(self):
        return _api_scrape(self.json, 0)


class TeamGeneralSplits(_TeamDashboard):
    _endpoint = 'teamdashboardbygeneralsplits'

    def location(self):
        return _api_scrape(self.json, 1)

    def wins_losses(self):
        return _api_scrape(self.json, 2)

    def monthly(self):
        return _api_scrape(self.json, 3)

    def pre_post_all_star(self):
        return _api_scrape(self.json, 4)

    def days_rest(self):
        return _api_scrape(self.json, 5)


class TeamOpponentSplits(_TeamDashboard):
    _endpoint = 'teamdashboardbyopponent'

    def by_conference(self):
        return _api_scrape(self.json, 1)

    def by_division(self):
        return _api_scrape(self.json, 2)

    def by_opponent(self):
        return _api_scrape(self.json, 3)


class TeamLastNGamesSplits(_TeamDashboard):
    _endpoint = 'teamdashboardbylastngames'

    def last5(self):
        return _api_scrape(self.json, 1)

    def last10(self):
        return _api_scrape(self.json, 2)

    def last15(self):
        return _api_scrape(self.json, 3)

    def last20(self):
        return _api_scrape(self.json, 4)

    def gamenumber(self):
        return _api_scrape(self.json, 5)


class TeamInGameSplits(_TeamDashboard):
    _endpoint = 'teamdashboardbygamesplits'

    def by_half(self):
        return _api_scrape(self.json, 1)

    def by_period(self):
        return _api_scrape(self.json, 2)

    def by_score_margin(self):
        return _api_scrape(self.json, 3)

    def by_actual_margin(self):
        return _api_scrape(self.json, 4)


class TeamClutchSplits(_TeamDashboard):
    """
    This is a weird endpoint, to be honest.
    It's got a lot of cool little stats and there are two extra
    fields in the json that I have no idea what they do.

    If you know please tell me.
        * Last30Sec3Point2TeamDashboard
        * Last10Sec3Point2TeamDashboard
    """
    _endpoint = 'teamdashboardbyclutch'

    def last5min_deficit_5point(self):
        """
        Results in last 5 minutes <= 5 points
        """
        return _api_scrape(self.json, 1)

    def last3min_deficit_5point(self):
        """
        Results in last 5 minutes <= 5 points
        """
        return _api_scrape(self.json, 2)

    def last1min_deficit_5point(self):
        """
        Results in last 5 minutes <= 5 points
        """
        return _api_scrape(self.json, 3)

    def last30sec_deficit_3point(self):
        """
        Results in last 5 minutes <= 5 points
        """
        return _api_scrape(self.json, 4)

    def last10sec_deficit_3point(self):
        """
        Results in last 5 minutes <= 5 points
        """
        return _api_scrape(self.json, 5)

    def last5min_plusminus_5point(self):
        """
        Last 5 minutes +/= 5 points
        """
        return _api_scrape(self.json, 6)

    def last3min_plusminus_5point(self):
        """
        Last 3 minutes +/= 5 points
        """
        return _api_scrape(self.json, 7)

    def last1min_plusminus_5point(self):
        """
        Last 1 minutes +/= 5 points
        """
        return _api_scrape(self.json, 8)

    def last30sec_plusminus_5point(self):
        """
        Last 30 seconds +/= 3 points
        """
        return _api_scrape(self.json, 9)


class TeamShootingSplits(_TeamDashboard):
    _endpoint = 'teamdashboardbyshootingsplits'

    def shot_5ft(self):
        return _api_scrape(self.json, 1)

    def shot_8ft(self):
        return _api_scrape(self.json, 2)

    def shot_areas(self):
        return _api_scrape(self.json, 3)

    def assisted_shots(self):
        return _api_scrape(self.json, 4)

    def shot_type_summary(self):
        return _api_scrape(self.json, 5)

    def assisted_by(self):
        return _api_scrape(self.json, 6)


class TeamPerformanceSplits(_TeamDashboard):
    _endpoint = 'teamdashboardbyteamperformance'

    def score_differential(self):
        return _api_scrape(self.json, 1)

    def points_scored(self):
        return _api_scrape(self.json, 2)

    def points_against(self):
        return _api_scrape(self.json, 3)


class TeamYearOverYearSplits(_TeamDashboard):
    _endpoint = 'teamdashboardbyyearoveryear'

    def by_year(self):
        return _api_scrape(self.json, 1)


class TeamLineups:
    _endpoint = 'teamdashlineups'

    def __init__(self,
                 team_id,
                 game_id='',
                 group_quantity=constants.GroupQuantity.Default,
                 season=constants.CURRENT_SEASON,
                 season_type=constants.SeasonType.Default,
                 measure_type=constants.MeasureType.Default,
                 per_mode=constants.PerMode.Default,
                 plus_minus=constants.PlusMinus.Default,
                 pace_adjust=constants.PaceAdjust.Default,
                 rank=constants.Rank.Default,
                 outcome=constants.Outcome.Default,
                 location=constants.Location.Default,
                 month=constants.Month.Default,
                 season_segment=constants.SeasonSegment.Default,
                 date_from=constants.DateFrom.Default,
                 date_to=constants.DateTo.Default,
                 opponent_team_id=constants.OpponentTeamID.Default,
                 vs_conference=constants.VsConference.Default,
                 vs_division=constants.VsDivision.Default,
                 game_segment=constants.GameSegment.Default,
                 period=constants.Period.Default,
                 last_n_games=constants.LastNGames.Default):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'GroupQuantity': group_quantity,
                                      'GameID': game_id,
                                      'TeamID': team_id,
                                      'Season': season,
                                      'SeasonType': season_type,
                                      'MeasureType': measure_type,
                                      'PerMode': per_mode,
                                      'PlusMinus': plus_minus,
                                      'PaceAdjust': pace_adjust,
                                      'Rank': rank,
                                      'Outcome': outcome,
                                      'Location': location,
                                      'Month': month,
                                      'SeasonSegment': season_segment,
                                      'DateFrom': date_from,
                                      'DateTo': date_to,
                                      'OpponentTeamID': opponent_team_id,
                                      'VsConference': vs_conference,
                                      'VsDivision': vs_division,
                                      'GameSegment': game_segment,
                                      'Period': period,
                                      'LastNGames': last_n_games})

    def overall(self):
        return _api_scrape(self.json, 0)

    def lineups(self):
        return _api_scrape(self.json, 1)


class TeamPlayers(_TeamDashboard):
    _endpoint = 'teamplayerdashboard'

    def season_totals(self):
        return _api_scrape(self.json, 1)


class TeamPlayerOnOffDetail(_TeamDashboard):
    _endpoint = 'teamplayeronoffdetails'

    def on_court(self):
        return _api_scrape(self.json, 1)

    def off_court(self):
        return _api_scrape(self.json, 2)


class TeamPlayerOnOffSummary(_TeamDashboard):
    _endpoint = 'teamplayeronoffsummary'

    def on_court(self):
        return _api_scrape(self.json, 1)

    def off_court(self):
        return _api_scrape(self.json, 2)


class TeamGameLogs:
    _endpoint = 'teamgamelog'

    def __init__(self,
                 team_id,
                 season=constants.CURRENT_SEASON,
                 season_type=constants.SeasonType.Default):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'TeamID': team_id,
                                      'Season': season,
                                      'SeasonType': season_type})

    def info(self):
        return _api_scrape(self.json, 0)


class TeamSeasons:
    _endpoint = 'teamyearbyyearstats'

    def __init__(self,
                 team_id,
                 league_id=constants.League.NBA,
                 season_type=constants.SeasonType.Default,
                 per_mode=constants.PerMode.Default):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'TeamID': team_id,
                                      'LeagueID': league_id,
                                      'SeasonType': season_type,
                                      'PerMode': per_mode})

    def info(self):
        return _api_scrape(self.json, 0)


class TeamShotTracking(_TeamDashboard):
    _endpoint = 'teamdashptshots'

    def shot_clock_shooting(self):
        return _api_scrape(self.json, 1)

    def dribble_shooting(self):
        return _api_scrape(self.json, 2)

    def closest_defender_shooting(self):
        return _api_scrape(self.json, 3)

    def closest_defender_shooting_long(self):
        return _api_scrape(self.json, 4)

    def touch_time_shooting(self):
        return _api_scrape(self.json, 5)


class TeamReboundTracking(_TeamDashboard):
    _endpoint = 'teamdashptreb'

    def shot_type_rebounding(self):
        return _api_scrape(self.json, 1)

    def contested_rebounding(self):
        return _api_scrape(self.json, 2)

    def shot_distance_rebounding(self):
        return _api_scrape(self.json, 3)

    def rebound_distance_rebounding(self):
        return _api_scrape(self.json, 4)


class TeamPassTracking(_TeamDashboard):
    _endpoint = 'teamdashptpass'

    def passes_made(self):
        return _api_scrape(self.json, 0)

    def passes_recieved(self):
        return _api_scrape(self.json, 1)


class TeamVsPlayer:
    _endpoint = 'teamvsplayer'

    def __init__(self,
                 team_id,
                 vs_player_id,
                 measure_type=constants.MeasureType.Default,
                 per_mode=constants.PerMode.Default,
                 plus_minus=constants.PlusMinus.Default,
                 pace_adjust=constants.PaceAdjust.Default,
                 rank=constants.Rank.Default,
                 league_id=constants.League.Default,
                 season=constants.CURRENT_SEASON,
                 season_type=constants.SeasonType.Default,
                 po_round=constants.PlayoffRound.Default,
                 outcome=constants.Outcome.Default,
                 location=constants.Location.Default,
                 month=constants.Month.Default,
                 season_segment=constants.SeasonSegment.Default,
                 date_from=constants.DateFrom.Default,
                 date_to=constants.DateTo.Default,
                 opponent_team_id=constants.OpponentTeamID.Default,
                 vs_conference=constants.VsConference.Default,
                 vs_division=constants.VsDivision.Default,
                 game_segment=constants.GameSegment.Default,
                 period=constants.Period.Default,
                 shot_clock_range=constants.ShotClockRange.Default,
                 last_n_games=constants.LastNGames.Default):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'TeamID': team_id,
                                      'VsPlayerID': vs_player_id,
                                      'MeasureType': measure_type,
                                      'PerMode': per_mode,
                                      'PlusMinus': plus_minus,
                                      'PaceAdjust': pace_adjust,
                                      'Rank': rank,
                                      'LeagueID': league_id,
                                      'Season': season,
                                      'SeasonType': season_type,
                                      'PORound': po_round,
                                      'Outcome': outcome,
                                      'Location': location,
                                      'Month': month,
                                      'SeasonSegment': season_segment,
                                      'DateFrom': date_from,
                                      'DateTo': date_to,
                                      'OpponentTeamID': opponent_team_id,
                                      'VsConference': vs_conference,
                                      'VsDivision': vs_division,
                                      'GameSegment': game_segment,
                                      'Period': period,
                                      'ShotClockRange': shot_clock_range,
                                      'LastNGames': last_n_games})

    def overall(self):
        return _api_scrape(self.json, 0)

    def vs_player_overall(self):
        return _api_scrape(self.json, 1)

    def on_off_court(self):
        return _api_scrape(self.json, 2)

    def shot_distance_overall(self):
        return _api_scrape(self.json, 3)

    def shot_distance_on_court(self):
        return _api_scrape(self.json, 4)

    def shot_distance_off_court(self):
        return _api_scrape(self.json, 5)

    def shot_area_overall(self):
        return _api_scrape(self.json, 6)

    def shot_area_on_court(self):
        return _api_scrape(self.json, 7)

    def shot_area_off_court(self):
        return _api_scrape(self.json, 8)


class TeamHustleLeaders:
    """
    Contains league leading hustle stats by team

    Args:
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular or Playoffs)
        :playoff_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :team_id: ID of the team to look up
        :conference: Filter by conference
        :division: Filter by division
        :player_experience: Player experience (Rookie
        :player_position: Filter by position (Forward
        :draft_year: Filter by draft year
        :draft_pick: Filter by draft pick (1st+Round, Lottery+Pick, etc.)
        :college: Filter by college
        :country: Filter by country
        :height: Filter by player's height
        :weight: Filter by player's weight
    """

    _endpoint = 'leaguehustlestatsteamleaders'

    def __init__(self,
                 per_mode=constants.PerMode.Default,
                 league_id=constants.League.Default,
                 season=constants.CURRENT_SEASON,
                 season_type=constants.SeasonType.Default,
                 playoff_round=constants.PlayoffRound.Default,
                 outcome=constants.Outcome.Default,
                 location=constants.Location.Default,
                 month=constants.Month.Default,
                 season_segment=constants.SeasonSegment.Default,
                 date_from=constants.DateFrom.Default,
                 date_to=constants.DateTo.Default,
                 opponent_team_id=constants.OpponentTeamID.Default,
                 vs_conference=constants.VsConference.Default,
                 vs_division=constants.VsDivision.Default,
                 team_id=constants.TeamID.Default,
                 conference=constants.Conference.Default,
                 division=constants.Division.Default,
                 player_experience=constants.PlayerExperience.Default,
                 player_position=constants.PlayerPosition.Default,
                 draft_year=constants.DraftYear.Default,
                 draft_pick=constants.DraftPick.Default,
                 college=constants.College.Default,
                 country=constants.Country.Default,
                 height=constants.Height.Default,
                 weight=constants.Weight.Default
                 ):

        self.json = _get_json(endpoint=self._endpoint,
                              params={  'PerMode': per_mode,
                                        'LeagueID': league_id,
                                        'Season': season,
                                        'SeasonType': season_type,
                                        'PORound': playoff_round,
                                        'Outcome': outcome,
                                        'Location': location,
                                        'Month': month,
                                        'SeasonSegment': season_segment,
                                        'DateFrom': date_from,
                                        'DateTo': date_to,
                                        'OpponentTeamID': opponent_team_id,
                                        'VsConference': vs_conference,
                                        'VsDivision': vs_division,
                                        'TeamID': team_id,
                                        'Conference': conference,
                                        'Division': division,
                                        'PlayerExperience': player_experience,
                                        'PlayerPosition': player_position,
                                        'DraftYear': draft_year,
                                        'DraftPick': draft_pick,
                                        'College': college,
                                        'Country': country,
                                        'Height': height,
                                        'Weight': weight
                                      })

    def contested_shots(self):
        return _api_scrape(self.json, 0)

    def charges_drawn(self):
        return _api_scrape(self.json, 1)

    def deflections(self):
        return _api_scrape(self.json, 2)

    def loose_balls(self):
        return _api_scrape(self.json, 3)

    def screen_assists(self):
        return _api_scrape(self.json, 4)


class TeamHustleStats:
    """
    Contains hustle stats by team

    Args:
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular or Playoffs)
        :playoff_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :team_id: ID of the team to look up
        :conference: Filter by conference
        :division: Filter by division
        :player_experience: Player experience (Rookie
        :player_position: Filter by position (Forward
        :draft_year: Filter by draft year
        :draft_pick: Filter by draft pick (1st+Round, Lottery+Pick, etc.)
        :college: Filter by college
        :country: Filter by country
        :height: Filter by player's height
        :weight: Filter by player's weight
    """

    _endpoint = 'leaguehustlestatsteam'

    def __init__(self,
                 per_mode=constants.PerMode.Default,
                 league_id=constants.League.Default,
                 season=constants.CURRENT_SEASON,
                 season_type=constants.SeasonType.Default,
                 playoff_round=constants.PlayoffRound.Default,
                 outcome=constants.Outcome.Default,
                 location=constants.Location.Default,
                 month=constants.Month.Default,
                 season_segment=constants.SeasonSegment.Default,
                 date_from=constants.DateFrom.Default,
                 date_to=constants.DateTo.Default,
                 opponent_team_id=constants.OpponentTeamID.Default,
                 vs_conference=constants.VsConference.Default,
                 vs_division=constants.VsDivision.Default,
                 team_id=constants.TeamID.Default,
                 conference=constants.Conference.Default,
                 division=constants.Division.Default,
                 player_experience=constants.PlayerExperience.Default,
                 player_position=constants.PlayerPosition.Default,
                 draft_year=constants.DraftYear.Default,
                 draft_pick=constants.DraftPick.Default,
                 college=constants.College.Default,
                 country=constants.Country.Default,
                 height=constants.Height.Default,
                 weight=constants.Weight.Default
                 ):

        self.json = _get_json(endpoint=self._endpoint,
                              params={  'PerMode': per_mode,
                                        'LeagueID': league_id,
                                        'Season': season,
                                        'SeasonType': season_type,
                                        'PORound': playoff_round,
                                        'Outcome': outcome,
                                        'Location': location,
                                        'Month': month,
                                        'SeasonSegment': season_segment,
                                        'DateFrom': date_from,
                                        'DateTo': date_to,
                                        'OpponentTeamID': opponent_team_id,
                                        'VsConference': vs_conference,
                                        'VsDivision': vs_division,
                                        'TeamID': team_id,
                                        'Conference': conference,
                                        'Division': division,
                                        'PlayerExperience': player_experience,
                                        'PlayerPosition': player_position,
                                        'DraftYear': draft_year,
                                        'DraftPick': draft_pick,
                                        'College': college,
                                        'Country': country,
                                        'Height': height,
                                        'Weight': weight
                                      })
