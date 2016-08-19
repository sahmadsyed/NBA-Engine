from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError

from main.views.helpers.current_season_stats_job import CurrentSeasonStatsJob


class PlayersList(APIView):
    """
    If request is valid, returns list of players based on supplied parameters.
    If request is invalid, returns error with appropriate message.

    Attributes:
        permission_classes (object): Specifies permissions needed to receive data

    """

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """
        Returns response to GET request for list of players based on request.

        Returns:
            object: Response object containing list of players and length of list

        """
        query_set = self._get_players()
        serializer = PlayerSerializer(query_set, many=True)
        resp_data = {'count' : len(query_set), 'players' : serializer.data}
        return Response(resp_data)

    def _get_players(self):
        """
        Helper function to retrieve list of players from DB based on request
        parameters.

        Returns:
            List[object]: List of Player objects meeting request parameters

        """
        query = Player.objects.all()
        name_ = self.request.query_params.get('name')
        draft_year_ = self.request.query_params.get('draft_year')
        position_ = self.request.query_params.get('position')
        if name_:
            query = query.filter(name__iexact = name_)
        if draft_year_:
            if not draft_year_.isdigit():
                raise ParseError('Draft year must be a positive integer')
            query = query.filter(year_enter_league = draft_year_)
        if position_:
            if position_.lower() not in ['center', 'forward', 'guard']:
                raise NotFound('Incorrect position')
            query = query.filter(position__iexact = position_)
        return query

class PastStatisticsList(APIView):
    """
    If request is valid, returns past stats of players based on supplied parameters.
    If request is invalid, returns error with appropriate message.

    Attributes:
        permission_classes (object): Specifies permissions needed to receive data

    """

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """
        Returns response to GET request for past stats based on request.

        Returns:
            object: Response object containing list of stats and length of list

        """
        query_set = self._get_stats()
        serializer = StatisticsSerializer(query_set, many=True)
        resp_data = {'count' : len(query_set), 'stats' : serializer.data}
        return Response(resp_data)

    def _get_stats(self):
        """
        Helper function to retrieve past stats from DB based on request
        parameters.

        Returns:
            List[object]: List of Statistics objects meeting request parameters

        """
        name_ = self.request.query_params.get('name')
        if not name_:
            raise ParseError('Missing \'name\'')
        season_ = self.request.query_params.get('season')
        query = Statistics.objects.filter(name__iexact = name_)
        if season_:
            season_ = str(season_)
            if not season_.isdigit():
                raise ParseError('Season must be a positive integer')
            formatted_season = '%s-%s' % (season_, str(int(season_) + 1)[-2:])
            query = query.filter(season = formatted_season)
        return query

class CurrentStatistics(PastStatisticsList):
    """
    If request is valid, returns current stats of players based on supplied parameters.
    If request is invalid, returns error with appropriate message.
    """

    def _get_stats(self):
        """
        Helper function to retrieve current stats from DB based on request
        parameters.

        Returns:
            List[object]: List of Statistics objects meeting request parameters

        """
        current_season_stats = CurrentSeasonStatsJob().get()
        name_ = self.request.query_params.get('name')
        if name_:
            name_ = name_.lower()
            stats = filter(lambda s: s.name.lower() == name_, current_season_stats)
            return stats
        else:
            return current_season_stats
