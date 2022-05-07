/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * client_api.h
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

#ifndef CLIENT_API_H_
#define CLIENT_API_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <coap.h>
#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <config.h>
#include <arpa/inet.h>

#define PROGRAM_NAME "coap_client"
#define SERVER_IP "127.0.0.1"
#define SERVER_PORT 5683
#define SERVER_URI "coap://127.0.0.1/time"
#define CLIENT_IP "0.0.0.0"
#define CLIENT_PORT 0
#define GET_METHOD 1
#define TIME_ONLY 0x74
#define DATE_ONLY 0x64
#define FULL_DATE 0x66
#define VERBOSE 0x76
#define HELP 0x68
#define KNRM "\x1B[0m"
#define KRED "\x1B[31m"
#define KGRN "\x1B[32m"
#define KYEL "\x1B[33m"
#define KBLU "\x1B[34m"
#define KMAG "\x1B[35m"
#define KCYN "\x1B[36m"
#define KWHT "\x1B[37m"

extern int verbose;

/**
 * Description:
 *     Process program options.
 *
 * Arguments:
 *     args - Number of arguments.
*      argv - Array of arguments.
 *
 * Return value:
 *     Option code number.
 */
int process_options(int argc, char* argv[]);

/**
 * Description:
 *     Print usage message to console stream.
 *
 * Arguments:
 *     stream    - FILE stream.
*      exit_code - Exit return code.
 *
 * Return value:
 *     None.
 */
void print_usage(FILE* stream, int exit_code);

/**
 * Description:
 *     Print verbose message to console stream.
 *
 * Arguments:
 *     verbose - Control flag for verbose message.
*      message - Message verbose content.
 *
 * Return value:
 *     None.
 */
void print_verbose(int verbose, const char* message);

/**
 * Description:
 *     Print error message to console stream.
 *
 * Arguments:
 *     message - Message error content.
 *
 * Return value:
 *     None.
 */
void print_error(const char* message);

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
void print_success(const char* message);

/**
 * Description:
 *     Getting current local time on host.
 *
 * Arguments:
 *     ctx - coap context
 *     local_interface - local interface
 *     remote - remote address
 *     sent - pdu sent
 *     received - pdu received
 *     id - coap id
 *
 * Return value:
 *     Current local time from host in string format | NULL.
 */
void time_handler(
    struct coap_context_t *ctx, const coap_endpoint_t *local_interface,
    const coap_address_t *remote, coap_pdu_t *sent, coap_pdu_t *received,
    const coap_tid_t id
);

#ifdef __cplusplus
}
#endif

#endif

