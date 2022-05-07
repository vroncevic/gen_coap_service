/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * print_success.c
 * Copyright (C) ${YEAR} Vladimir Roncevic <elektron.ronca@gmail.com>
 *
 * ${PRO} is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * ${PRO} is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program. If not, see <http://www.gnu.org/licenses/>.
 */

#include "client_api.h"

/**
 * Description:
 *     Print success message to console stream.
 *
 * Arguments:
 *     message - Message success content.
 *
 * Return value:
 *     None.
 */
void print_success(const char* message) {
    fprintf(stdout, "%s", KGRN);
    fprintf(stdout, "%s\n", message);
    fprintf(stdout,"%s", KNRM);
}

